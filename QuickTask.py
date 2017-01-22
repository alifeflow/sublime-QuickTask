import sublime
import sublime_plugin
import re, subprocess

class quick_task_openCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		line = self.view.substr(self.view.line(self.view.sel()[0]))
		# print("The selected line is:"+line)

		marks = re.search("^\s*[DOING|DONE]*", line)
		if (marks is not None):
			mark = marks.group(0)
		# Update the mark
		command = re.sub("^\s*[DOING|DONE]*", "", line)
		# Open the command
		print("Command is："+command)
		subprocess.Popen("cmd.exe /C" + command, shell=False)
		# subprocess.Popen("cmd.exe", shell=False)