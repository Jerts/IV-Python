using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace gaussian2
{
    class Program
    {
        static double[] Gauss(ref double[] time, int m=0,int s=2)
        {
            double[] result = new double[time.Length];
            for(int i = 0; i<time.Length; i++)
            {
                result[i] = (1 / (Math.Sqrt(2 * Math.PI) * s)) * Math.Exp((-0.5) * Math.Pow((time[i] - m) / s, 2));
            }
            return result;
        }
        static void GetEvenlyDistPoints(int numPoins, double min, double max, ref double[] lista)
        {
            lista[0] = min;
            double increment = (max - min) / (numPoins - 1);
            for(int i = 1; i < numPoins-1; i++)
            {
                lista[i] = lista[i - 1] + increment;
            }
            lista[lista.Length - 1]=max;
        }
        static void Main(string[] args)
        {
            int m = 0;
            int s = 2;
            int n = 12;
            double[] puntos = new double[n];
            GetEvenlyDistPoints(n, m - 5*s, m + 5*s, ref puntos);
            double[] resultados = new double[n];
            resultados = Gauss(ref puntos, m, s);
            for(int i = 0; i<n; i++)
            {
                Console.WriteLine("En el punto: {0} la funcon es {1}",puntos[i],resultados[i]);
            }
        }
    }
}
