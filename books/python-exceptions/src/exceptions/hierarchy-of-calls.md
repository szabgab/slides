# Hierarchy of calls


```
main()
    some_process()
        for filename in some_list:
            handle_file(filename)
                private_module.deal_with_file(filename)
                    private_module._helper_function(filename)
                       public_module.process_file(filename)
                           with open(filename) as fh:
                               pass
```


