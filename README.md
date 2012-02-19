# SublimeBlockCursor #

![Screenshot](http://f.cl.ly/items/42131K2X1h0j0P2m1O2B/Screen%20Shot%202011-12-02%20at%202.36.54%20AM.png)

When using "Vintage Mode" in [Sublime Text 2][sublime], it can become very difficult to keep track of your cursor location. In vim this is solved by having a "block" cursor, which is very easy to spot no matter where it is on screen. Unfortunately, Sublime Text 2 does not (yet) support this feature natively. This Plugin mimics this functionality by highlighting the area behind the cursor whenever it moves (similar to how you might highlight syntax errors, or color a comment).

## Installation ##

### With Package Control ###

If you have the [Package Control][package_control] installed, you can install SublimeBlockCursor from inside Sublime Text itself. Open the Command Palette and select "Package Control: Install Package", then search for SublimeBlockCursor and you’re done!

### Without Package Control ###

Go to your Sublime Text 2 Packages directory:

	Windows: %USERPROFILE%\AppData\Roaming\Sublime Text 2\Packages\
	Mac: ~/Library/Application Support/Sublime Text 2/Packages/	

and clone the repository there
	
	git clone git://github.com/netpro2k/SublimeBlockCursor


## Configuration ##

You can change the style of the block cursor by adding a section to your theme file like so:

```xml
<dict>
	<key>name</key>
	<string>Block Cursor</string>
	<key>scope</key>
	<string>block_cursor</string>
	<key>settings</key>
	<dict>
		<key>foreground</key>
		<string>#212121</string>
		<key>background</key>
		<string>#9ca9b7</string>
	</dict>
</dict>
```

---------

[sublime]: http://www.sublimetext.com/2
[package_control]: http://wbond.net/sublime_packages/package_control
