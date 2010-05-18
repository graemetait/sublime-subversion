Sublime Subversion
==================

A very basic Subversion client for the [Sublime Text](http://www.sublimetext.com/) text editor.

The aim is to provide a quick method to commit simple changes without leaving Sublime.  To this end the only subversion commands that are supported are 'status', to check what will be commited, 'add', to add new files to the commit, and 'commit'.

Committing will show you a diff of your changes, and allow you to enter a single line of text for the commit message.

I'm not a Python programmer, so this is mostly hacked together from other Sublime plugins (mainly [Mercurial](http://sublime-text-community-packages.googlecode.com/svn/pages/Mercurial.html)) just to scratch my own itch.


Usage
-----

 * Copy both files in to your 'Sublime Text/Packages/User' folder which you should be able to find in your profile folder.
 * Make sure that you have the subversion command line client installed and that it's in your path.
 * All commands are accessed via keyboard shortcuts, which you can view/change by opening Default.sublime-keymap.


Known Issues
------------

Very occasionally Sublime will freeze when generating the diff.  Killing the svn.exe will bring Sublime back to life.