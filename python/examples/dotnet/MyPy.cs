using System;

//namespace hello_world_csharp
//{
//    class Program
//    {
		static void Main(string[] args)
		{
			using (Py.GIL())
			{
				dynamic np = Py.Import("numpy");
				Console.WriteLine(np.cos(np.pi * 2));

				dynamic sin = np.sin;
				Console.WriteLine(sin(5));

				double c = np.cos(5) + sin(5);
				Console.WriteLine(c);

				dynamic a = np.array(new List<float> { 1, 2, 3 });
				Console.WriteLine(a.dtype);

				dynamic b = np.array(new List<float> { 6, 5, 4 }, dtype: np.int32);
				Console.WriteLine(b.dtype);

				Console.WriteLine(a * b);
				Console.ReadKey();
			}
		}
//	}
//}
// From https://github.com/pythonnet/pythonnet
