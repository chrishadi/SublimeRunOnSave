SublimeRunOnSave
======================

This is another Sublime Text 3 plugin to run any shell command on file save event.

This plugin is inspired by <a href="http://www.purplebeanie.com/Development/automatically-run-build-on-save-in-sublime-text-2.html">Build-on-Save</a> plugin from a post in purplebeanie.com and <a href="https://github.com/alexnj/SublimeOnSaveBuild">SublimeOnSaveBuild</a> by Alex N. Jose.

The best use case for this plugin is probably in TDD (Test Driven Development) process where you want Sublime to automatically run the test when you save a file.


How to use this plugin:
-----------------------

At the very minimum, you just need to put the "runonsave.py" in a sub directory of your Sublime Text 3 Packages folder (e.g.: ~/.config/sublime-text-3/Packages/YourSubdirectoryName). Or, while in the Packages folder you might want to do this:
```
git clone git://github.com/chrishadi/SublimeRunOnSave.git
```
Voila, you have just install a new plugin by cloning this github repository!

Now we get to the settings part.

Create a Sublime Project (using "Save Project As" command from "Project" menu), and then edit the project (Project > Edit Project) so that the project configuration resembles something like this:
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
As you might have already guessed by now, we enable the plugin by assigning "run_on_save" the value of 1. Then, we specify the command to be run in the form of an array containing the program name as the first element and its parameter as the next element. That is equivalent to typing into a shell terminal a command of "phpunit test.php".

You can also set the working directory of the project explicitly, to ensure that the command will always be invoked in the correct directory. To set the working directory, add the "folders" entry in the project configuration as follows (it is actually a common setting for a project in Sublime Text):
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

The last defined setting for this plugin is the "environment_variables". Here you can set alternative environment variables to complement or replace the system environment variables temporarily. The environment variables should be specified as an array of key-value pairs. The example below redefines the "HOSTNAME" and "UID" variables, if your Sublime Text is the Linux/Mac version.
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
		"environment_variables":
		[
			"HOSTNAME": "test_machine",
			"UID"     : 1001,
		]
	}
}
```
