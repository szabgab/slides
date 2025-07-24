from Bio.Seq import Seq

what_is_this = Seq("AGTC_U")
what_is_this.complement()  # ValueError: Mixed RNA/DNA found