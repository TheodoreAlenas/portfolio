# Portfolio website

[It's served](https://theodoros-d-alenas.site/)
on my rented server.

Features:

- no build step for English
- a build step for Greek translation
- fully accessible in browsers from 2015 and later
- a code style specifically for small projects
- dark, light and high contrast color schemes
- mobile support
- minimal code listings with custom highlights

The design is
[inspired by an image on Dribble](https://dribbble.com/shots/24399369-Case-Study-Minimal-Portfolio-Landing-Page)
of a project by
[Al Razi Siam.](http://alrazisiam.com/)

The dark color scheme is partly inspired by the
[dark theme of Rust's documentation.](https://doc.rust-lang.org/std/keyword.mut.html)
The high contrast scheme is definitely inspired by
the custom made Emacs theme that Mista Azosin made, called
[Gruber Darker.](https://github.com/rexim/gruber-darker-theme)
Mista has the
[Tsoding Daily YouTube channel.](https://www.youtube.com/@TsodingDaily)
I'd like to take full credit for the light scheme.

Some SVG icons were drawn using
[Inkscape.](https://inkscape.org/)

## Copying

To modify this portfolio,
I'd recommend that you try to write text that looks similar.
If the title has more bold letters it may look heavy,
if there are more code examples then maybe
you'd want to automate syntax highlighting to some degree,
if you have fewer links they may look forced and so on.
I find it impossible to just copy someone else's site.

I wanted no build steps, at least most of the time,
and I'm decent with CSS and the HTML basics.
I also wanted to have as few files as possible
*since* they would be few regardless,
because then it's easy to navigate through the code.
So, to have few files, I had to choose between a few designs
that could potentially be coded with little code.
There's also a specific aesthetic,
I wanted to sound chill.
I'm not sure you can tweak the page to make it more
energetic or determined. It's probably stuck like this.

With that, you may copy `index.html` from this repository,
open a browser window on the path where it's downloaded,
`file:///home/.../index.html`,
tweak it with a code editor, save and refresh the browser tab.

You'll need to set the indentation to zero.
You *need* to try it.
It feels like that's how you're meant to write HTML.
In Emacs that's `C-: (setq sgml-basic-offset 0)`
and in Vim it got to be `:set shiftwidth 0` I suppose.
In IntelliJ IDEA I'd try pressing shift twice,
I remember that pops up a list of options,
in VSCode the equivalent is `Ctrl + Shift + P`
I think and if you can't set such a setting,
you may want to consider using Notepad
or some other simple text editor.
