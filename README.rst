Introduction
============

.. image:: https://secure.travis-ci.org/pyrenees/plone.synchronize.png
   :target: http://travis-ci.org/pyrenees/plone.synchronize

This package provides a simple decorator to help synchronize methods across
threads, to avoid problems of concurrent access.

It can be used like this::

    from threading import Lock
    from plone.synchronize import synchronized

    class StupidStack(object):

        _elements = [] # not thread safe
        _lock = Lock()

        @synchronized(_lock)
        def push(self, item):
            self._elements.append(item)

        @synchronized(_lock)
        def pop(self):
            last = self._elements[-1]
            del self._elements[-1]
            return last

The decorator takes care of calling lock.acquire() just before the method
is executed, and lock.release() just after. If an exception is raised in the
method, the lock will still be released.
