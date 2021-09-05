using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _3_11
{
    class Program
    {
        static double Area(double[,] vertices)
        {
            return (1 / 2.0) * ( (vertices[1,0]*vertices[2,1])- (vertices[2, 0] * vertices[1, 1])- (vertices[0, 0] * vertices[2, 1])+ (vertices[2, 0] * vertices[0, 1])+ (vertices[0, 0] * vertices[1, 1])- (vertices[1, 0] * vertices[0, 1]));
            
        }
        static void Main(string[] args)
        {
            double[,] arreglo = { { 0, 0 }, { 1, 0 }, { 0, 1 } };
            Console.WriteLine(Area(arreglo));
        }
    }
}
