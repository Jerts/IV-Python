using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;
namespace _3_12
{
    class Program
    {
        static double Pathlength(ref int[] x, ref int[] y)
        {
            double acc=0;
            for (int i = 1; i < x.Length; i++)
            {
                acc = acc + Math.Sqrt(Math.Pow(x[i] - x[i - 1], 2) + Math.Pow(y[i] - y[i - 1], 2));
            }
            return acc;
        }
        static void Test_Pathlength(ref int[] x, ref int[] y)
        {
            if (Pathlength(ref x, ref y) == 7)
            {
                Console.WriteLine("El metodo regresa el valor esperado");
            }
            else
            {
                Console.WriteLine("El metodo regresa un valor erroneo");
            }
        }
        static void Main(string[] args)
        {
            int[] x_points = { 0, 4, 6 };
            int[] y_points = { 0, 3, 3 };

            Test_Pathlength(ref x_points, ref y_points);

        }
    }
}