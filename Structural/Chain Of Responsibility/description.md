This pattern is useful when you have a group of objects that can each handle a request in different ways, you want to avoid tightly coupling the objects together.

It allows you to pass requests along a chain of objects, each of which can handle the request or/and pass it on the next object in the chain.
