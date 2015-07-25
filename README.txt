Description
===========

Classica is a simple template library

Structure of template file should look like this:

(MyFirstTemplate)
    <p>This is your #@foo1 classica template</p>
    <p>Is it #@foo2?</p>
#!
(MySecondTemplate)
    <p>This is your #@foo classica template</p>
#!

There:
	"(MyFirstTemplate)" - name of template
	"#@foo1" - name of variable
	"#!" - end of template

Structure of template file should look like this:

#!(STG)/output.html|/input_templates.classica#!
#!(MyFirstTemplate)first|simple#!

"|" -uses to separate variables