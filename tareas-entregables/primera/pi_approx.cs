using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _3_13
{
    class Program
    {
        static double Pathlength(ref double[] x, ref double[] y)
        {
            double acc = 0;
            for (int i = 1; i < x.Length; i++)
            {
                acc = acc + Math.Sqrt(Math.Pow(x[i] - x[i - 1], 2) + Math.Pow(y[i] - y[i - 1], 2));
            }
            return acc;
        }
        static void GetCirclePoints(ref double[] puntos_x, ref double[] puntos_y ,int n)
        {
            for(int i = 0; i < n+1; i++)
            {
                puntos_x[i] = (0.5) * Math.Cos(2 * Math.PI * i / n);
                puntos_y[i] = (0.5) * Math.Sin(2 * Math.PI * i / n);
               
            }
        }
        static void Main(string[] args)
        {
            int k = 5;
            int n = (int)Math.Pow(2, k);
            double pi = 0;
            Console.WriteLine("N es : "+n);
            double[] puntos_x = new double[n+1];
            double[] puntos_y = new double[n+1];
            GetCirclePoints(ref puntos_x,ref puntos_y, n);
            pi = Pathlength(ref puntos_x, ref puntos_y);
            Console.WriteLine("El error es " + (Math.PI- pi).ToString());
            
        }
    }
}
