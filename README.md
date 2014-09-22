SublimeRunOnSave
======================

This is another Sublime Text 3 plugin to run any shell command on file save event.

This plugin is inspired by <a href="http://www.purplebeanie.com/Development/automatically-run-build-on-save-in-sublime-text-2.html">Build-on-Save</a> plugin from a post in purplebeanie.com and <a href="https://github.com/alexnj/SublimeOnSaveBuild">SublimeOnSaveBuild</a> by Alex N. Jose.

The best use case for this plugin is (probably) in TDD (Test Driven Development) process where you want Sublime to automatically run the test when you save a file.


How to use this plugin:
-----------------------

At the very minimum, you just need to put the "runonsave.py" in a sub directory of your Sublime Text 3's Packages folder (e.g.: ~/.config/sublime-text-3/Packages/YourSubdirectoryName). Or, while in the Packages folder you might want to do this:
```
git clone git://github.com/chrishadi/SublimeRunOnSave.git
```
Voila, you have a new plugin!

Here comes the settings part.

Create a Sublime Project (using "Save Project As" command from "Project" menu), and then edit the project (Project > Edit Project) so that the project configuration resemble something like this:
```javascript
{
	"settings":
	{
		"run_on_save": 1,
		"command":
		[
			"phpunit",
			"test.php"
		]
	}
}
```
Bravo!
You have the minimal working settings to run this plugin.

The "command" setting above is an array consists of the program name you wish to run as the first element and its parameter following as the next array element. That is quivalent to typing into a shell terminal a command of "phpunit test.php".

You can also set the working directory of the project explicitly, so the plugin will rely on that setting and the command doesn't get run in the wrong directory. That run-in-the-wrong-path accident might happen when you open a file that doesn't belong to the current project (thus, doesn't reside in the project's directory) and then perform a Save action. Sublime sometimes runs a command within the context of a file's path. To set the working directory you add the "folders" entry in the project configuration as follows (it is a common setting for any project in Sublime Text):
```javascript
{
	"folders":
	[
		{
			"path": "your_project_path_here"
		}
	],
	"settings":
	{
		"run_on_save": 1,
		"command":
		[
			"phpunit",
			"test.php"
		]
	}
}
```

The last defined setting for this plugin is the "environment_variables". Here you can set environment variables to replace the shell environment variables temporarily. The environment variables should be specified as an array of "key: value" pairs. The complete setting with the environment variables defined wil be something like this:
```javascript
{
	"folders":
	[
		{
			"path": "your_project_path_here"
		}
	],
	"settings":
	{
		"run_on_save": 1,
		"command":
		[
			"phpunit",
			"test.php"
		],
		"environment_variables:
		[
			"HOSTNAME": "test_machine",
			"UID"     : 1001,
		]
	}
}
```
