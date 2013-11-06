from Constants import*
import traceback

class StdoutProxy():
    def __init__(self, writeFunc):
        self.writeFunc = writeFunc
        self.skip = False

    def flush(self):
        pass

    def write(self, text):
        if not self.skip:
            strippedText = text.rstrip('\n')
            self.writeFunc(strippedText)
            QtCore.QCoreApplication.processEvents()
        self.skip = not self.skip

class Console(QtGui.QPlainTextEdit):
    MONOSPACE_FONT = 'Lucida Console'
    def __init__(self, prompt='>> ', message='', parent=None):
        super(Console, self).__init__(parent)

        self.history = []
        self.namespace = {}
        self.construct = []

        self.prompt = prompt
        self.setGeometry(50, 50, 600, 150)
        self.setWordWrapMode(QtGui.QTextOption.WrapAnywhere)
        self.setUndoRedoEnabled(False)
        self.document().setDefaultFont(QtGui.QFont(self.MONOSPACE_FONT, 10, QtGui.QFont.Normal))
        self.showMessage(message)
        self.updateNamespace({'run' : self.runScript})

    def setJson(self, json):
        self.isJson = json

    def runScript(self, fileName):
        with open(fileName) as f:
            script = f.read()
        result = eval(script, self.namespace, self.namespace)

    def updateNamespace(self, namespace):
        self.namespace.update(namespace)

    def showMessage(self, message):
        self.appendPlainText(message)
        self.newPrompt()

    def newPrompt(self):
        if self.construct:
            prompt = '.'*len(self.prompt)
        else:
            prompt = self.prompt

        self.completionsPosition = self.textCursor().position()
        self.completionsVisible = False

        self.appendPlainText(prompt)
        self.moveCursor(QtGui.QTextCursor.End)

    def clear(self):
        self.setPlainText('')
        self.newPrompt()

    def getCommand(self):
        document = self.document()
        currentLine = unicode(document.findBlockByLineNumber(
            document.lineCount()-1).text())
        currentLine = currentLine.rstrip()
        currentLine = currentLine[len(self.prompt):]
        return currentLine

    def setCommand(self, command):
        if self.getCommand() == command:
            return

        document = self.document()
        currentLine = unicode(document.findBlockByLineNumber(
            document.lineCount()-1).text())
        self.moveCursor(QtGui.QTextCursor.End)
        for i in range(len(currentLine)-len(self.prompt)):
            self.moveCursor(QtGui.QTextCursor.Left, QtGui.QTextCursor.KeepAnchor)

        self.textCursor().removeSelectedText()
        self.textCursor().insertText(command)
        self.moveCursor(QtGui.QTextCursor.End)

    def registerCommand(self, cursor, function):
        methods = {cursor : function}
        self.updateNamespace(methods)

    def showCompletions(self, completions):
        if self.completionsVisible:
            self.hideCompletions()

        cursor = self.textCursor()
        cursor.setPosition(self.completionsPosition)

        completions = map(lambda x: x.split('.')[-1], completions)
        t = '\n' + ' '.join(completions)
        if len(t) > 100:
            t = t[:100] + '...'
        cursor.insertText(t)
        self.completionsEnd = cursor.position()

        self.moveCursor(QtGui.QTextCursor.End)
        self.completionsVisible = True

    def hideCompletions(self):
        if not self.completionsVisible:
            return
        cursor = self.textCursor()
        cursor.setPosition(self.completionsPosition)
        l = self.completionsEnd - self.completionsPosition
        for x in range(l):
            cursor.deleteChar()

        self.moveCursor(QtGui.QTextCursor.End)
        self.completionsVisible = False

    def getCursorPosition(self):
        cursor = self.textCursor()
        return cursor.position() - cursor.block().position() - len(self.prompt)

    def setCursorPosition(self, position):
        self.moveCursor(QtGui.QTextCursor.StartOfLine)
        for i in range(len(self.prompt) + position):
            self.moveCursor(QtGui.QTextCursor.Right)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Tab:
            self.completions()
            return

        self.hideCompletions()

        if QKeyEvent.key() in (QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return):
            self.runCommand()
            return
        if QKeyEvent.key() == QtCore.Qt.Key_Home:
            self.setCursorPosition(0)
            return
        if QKeyEvent.key() in (QtCore.Qt.Key_Left, QtCore.Qt.Key_Backspace):
            if self.getCursorPosition() == 0:
                return
        elif QKeyEvent.key() == QtCore.Qt.Key_Up:
            #self.setCommand(self.getPrevHistoryEntry())
            return
        elif QKeyEvent.key() == QtCore.Qt.Key_Down:
            #self.setCommand(self.getNextHistoryEntry())
            return
        elif QKeyEvent.key() == QtCore.Qt.Key_Return:
            self.clear()
        super(Console, self).keyPressEvent(QKeyEvent)

    def completions(self):
        command = self.getCommand()
        lastword = re.split(' |\(|\)', command)[-1]
        beginning = command[0:-len(lastword)]

        path = lastword.split('.')
        namespaces = self.namespace.keys()

        if len(path) == 1:
            namespaces = namespaces
            prefix = ''
        else:
            obj = self.namespace.get(path[0])
            prefix = path[0] + '.'
            namespaces = dir(obj)

        completions = []

        for x in namespaces:
            if x[0] == '_' : continue
            xx = prefix + x
            if xx.startswith(lastword):
                completions.append(xx)
        completions.sort()

        if not completions:
            self.hide_completions()
        elif len(completions) == 1:
            self.hide_completions()
            self.setCommand(beginning + completions[0])
        else:
            p = os.path.commonprefix(completions)
            if len(p)>len(lastword):
                self.hide_completions()
                self.setCommand(beginning + p)
            else:
                self.show_completions(completions)

    def getHistory(self):
        return self.history

    def setHistory(self, history):
        self.history = history

    def addToHistory(self, command):
        if command and (not self.history or self.history[-1] != command):
            self.history.append(command)
        self.currentIndex = len(self.history)

    def getPreviousHistoryEntry(self):
        if self.history:
            self.currentIndex = max(0, (self.currentIndex-1))
            return self.history[self.currentIndex]
        return ''

    def getNextHistoryEntry(self):
        if self.history:
            currentLen = len(self.history)
            self.currentIndex = min(currentLen, self.currentIndex+1)
            if self.currentIndex < currentLen:
                return self.history[self.currentIndex]
        return ''

    def getConstruct(self, command):
        if self.construct:
            previousCommand = self.construct[-1]
            self.construct.append(command)
            if not previousCommand and not command:
                value = '\n'.join(self.construct)
                self.construct = []
                return value
            else:
                return ''
        else:
            if command and command[-1] == ':':
                self.construct.append(command)
                return ''
            else:
                return command

    def runCommand(self):
        command = self.getCommand()
        self.addToHistory(command)
        command = self.getConstruct(command)

        if command:
            out = sys.stdout
            if type(self.namespace.get(command)) == type(lambda:None):
                self.appendPlainText("'%s' is a function. Type '%s()' to use it in console." %
                    (command, command))
                self.newPrompt()
                return

            sys.stdout = StdoutProxy(self.appendPlainText)
            try:
                try:
                    result = eval(command, self.namespace, self.namespace)
                    if result is not None:
                        if self.isJson:
                            print(result)
                        else:
                            self.appendPlainText(repr(result))
                except SyntaxError:
                    exec command in self.namespace
            except SystemExit:
                self.close()
            except:
                tracebackLines = traceback.format_exc().split('\n')
                for i in (3,2,1,-1):
                    tracebackLines.pop(i)
                self.appendPlainText('\n'.join(tracebackLines))
            sys.stdout = out
        self.newPrompt()
        self.setJson(False)

msg = '''
-- -- -- Console -- -- --
'''

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    console = Console(message = msg)
    console.updateNamespace({'var1':app, 'var2': 1234})
    console.show()
    sys.exit(app.exec_())
