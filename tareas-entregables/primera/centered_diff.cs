using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace centered_diff
{
    
    class Program
    {
        //delegate para encapsular a las funciones y usarlas como callbacks
        public delegate double Del(double x);
        static double Diff(Del f, double x, double h)
        {
            return (f(x + h) - f(x - h)) / (2.0 * h);
        }
        static void test_diff(Del f,double x, double h, double expected)
        {
            double test = Diff(f, x, h);
            Console.WriteLine("Expected value: " + expected + ", returned by diff(): "+test+", error="+(expected-test));
        }
        static double fun1(double x)
        {
            return Math.Exp(x);
        }
        static double fun2(double x)
        {
            return Math.Exp(-2.0*Math.Pow(x,2.0));
        }
        static double fun3(double x)
        {
            return Math.Cos(x);
        }
        static double fun4(double x)
        {
            return Math.Log(x);
        }
        static void Main(string[] args)
        {
            Del f1 = fun1;
            Del f2 = fun2;
            Del f3 = fun3;
            Del f4 = fun4;
            test_diff(f1, 0, 0.01, 1);
            test_diff(f2, 0, 0.01, 0);
            test_diff(f3, 2.0 * Math.PI, 0.01, 0);
            test_diff(f4, 1, 0.01, 1);
        }
    }
}
