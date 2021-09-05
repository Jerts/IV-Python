using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace sinesum1
{
    class Program
    {
        static void GetEvenlyDistPoints(int numPoins, double min, double max, ref double[] lista)
        {
            lista[0] = min;
            double increment = (max - min) / (numPoins - 1);
            for (int i = 1; i < numPoins - 1; i++)
            {
                lista[i] = lista[i - 1] + increment;
            }
            lista[lista.Length - 1] = max;
        }
        static double[] S(ref double[] time,int n_iter, double T)
        {
            double[] aux_list = new double[time.Length];
            double aux_acc = 0;
            
            for(int j=0; j<time.Length; j++)
            {
                for (int i = 1;i <= n_iter; i++)
                {//Recordar siempre poner los numeros como dobles ej 2.0
                    aux_acc = aux_acc + (1.0 / ((2 * i) - 1)) * Math.Sin((2.0 * (2 * i - 1) * Math.PI * time[j]) / T);
                }
                aux_list[j] = (4 / Math.PI) * aux_acc ;
                aux_acc = 0;
            }
            return aux_list;
        }
        static double[] f(ref double[] t,double T) {
            double[] aux_list = new double[t.Length];
            for (int i = 0; i< t.Length;i++) 
            {
                if (t[i] > 0 && t[i] < T / 2) 
                {
                    aux_list[i] = 1;
                }
                else if (t[i] == T / 2) 
                {
                    aux_list[i] = 0;
                }
                else if (t[i] > T / 2 && t[i]<T) 
                {
                    aux_list[i] = -1;
                }
                else 
                {
                    Console.WriteLine("t out of range, error on the arguments!!");
                }
            }
            return aux_list;
        }
        static void Main(string[] args)
        {
            int n = 5;
            double T = 2 * Math.PI;
            double[] alpha = new double[50];
            GetEvenlyDistPoints(alpha.Length, 0.01, 0.99, ref alpha);
      
            double[] t = new double[alpha.Length];
            
            for (int i = 0; i< t.Length; i++)
            {
                t[i] = T * alpha[i];
            }
       
            double[] St = S(ref t, n, T);
            double[] ft = f(ref t, T);

            Console.WriteLine("N# |f(t)|S(t)|err|");
            Console.WriteLine("-------------------------");
            for(int i = 0; i < St.Length; i++)
            {
                Console.WriteLine("{0} | {1} | {2} | {3} ",i,ft[i],St[i],ft[i]-St[i]);
            }
        }
    }
}
