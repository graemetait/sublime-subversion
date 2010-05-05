import sublime, sublimeplugin, sys, os, subprocess

class SubversionCommand(sublimeplugin.TextCommand):
	def run(self, view, args):
		window = sublime.activeWindow()
		project_file = window.project().fileName()
		os.chdir(os.path.dirname(project_file))
		if(args[0] == "status" or args[0] == "add"):
			if(args[0] == "status"):
				svn_cmd = "svn status"
			elif(args[0] == "add"):
				svn_cmd = "svn add \""+view.fileName()+"\""
			svn_output = getOutputOfSysCommand(svn_cmd)
			sublime.messageBox(svn_output)
		elif(args[0] == "commit"):
			svn_diff = getOutputOfSysCommand("svn diff")
			if(svn_diff == ""):
				sublime.messageBox("No changes to commit")
			else:
				createWindowWithText(view, svn_diff)
				window.showInputPanel("svn commit", "message here", self.commit, None, self.commitCancelled)
	
	def commitCancelled(self):
		sublime.messageBox("Commit cancelled")
		
	def commit(self, message):
		svn_output = getOutputOfSysCommand("svn commit -m \""+message+"\"")
		sublime.runCommand("close")
		sublime.messageBox("Commit successful")

def getOutputOfSysCommand(commandText):
	p = subprocess.Popen(commandText, shell=True, bufsize=1024, stdout=subprocess.PIPE)
	p.wait()
	stdout = p.stdout
	return stdout.read()

# Open a new buffer containing the given text			
def createWindowWithText(view, textToDisplay):
	SvnView = sublime.Window.newFile(view.window())
	SvnView.insert(SvnView.size(), textToDisplay)
	SvnView.setScratch(True)
	SvnView.setReadOnly(True)
	SvnView.setName("svn diff")
	return SvnView.id()