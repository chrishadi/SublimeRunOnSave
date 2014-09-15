SublimeRunOnSave
======================

Sublime Text 3 plugin to run any shell command on file save event.

This plugin is inspired by Build-on-Save plugin in a purplebeanie.com post (http://www.purplebeanie.com/Development/automatically-run-build-on-save-in-sublime-text-2.html) and SublimeOnSaveBuild by Alex N. Jose (https://github.com/alexnj/SublimeOnSaveBuild).

The best use case of this plugin is (probably) in TDD (Test Driven Development) process where you want Sublime to automatically run the test when you save a file.

How to use this plugin:

Basically you just need to put the .py file in your Sublime Text 3 Packages/User directory (e.g.: ~/.config/sublime-text-3/Packages/User/runonsave.py). Or, you can do this while in its parent directory (~/.config/sublime-text-3/Packages/):
```
git clone git://github.com/chrishadi/SublimeRunOnSave.git
```
For you who are not familiar with Git commands, just create a .py file (yes, the name before .py doesn't matter) and put the text from "runonsave.py" into it. Voila, now you have new plugin.

Now, comes the settings part:

Create a Sublime Project (using "Save Project As" command from Sublime's Project menu), and then edit the project (Project > Edit Project) to resemble something like this (replace "phpunit" and "test.php" with your test framework and test file to run):
```javascript
{
	"settings":
	{
		"run_on_save": 1,
		"command":
		[
			"phpunit",
			"test.php" // this is the filename containing a class that extends PHPUnit_Framework_TestCase
		]
	}
}
```
This is the minimal settings.

There are additional options you can put in there though, but I'm in a hurry now, I will add those later.

See you.
