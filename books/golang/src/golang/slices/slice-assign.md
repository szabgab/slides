# Slice Assign

* It is an alias to the other slice, same place in memory


Unlike with arrays, when we assign a slice, we only assign the location of the slice in the memory. So if we change the content of one of the slices then the other one also sees the change. 


{% embed include file="src/examples/slice-assign/slice_assign.go" %}
{% embed include file="src/examples/slice-assign/slice_assign.out" %}


