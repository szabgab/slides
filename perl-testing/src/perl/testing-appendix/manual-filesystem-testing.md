# File System testing

When testing a file system one wants to make sure that
the system operates reliably under various conditions. In no case will
it loose data, not even in extreme cases such as many small files or few
large files that could fill an entire disk.

Applications should be prepared for testing. For example in a Windows GUI application every
control should have a unique and persistent name so we can use that name to find the handle.
Testing the fact that every is control has a name is already one element in our testing suit.

