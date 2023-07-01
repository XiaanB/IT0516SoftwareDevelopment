class OverloadExample
    {
        public int DoCalculation(int length, int height)
        {
            return length * height;
        }
 
        public int DoCalculation(int length, int height, int depth)
        {
            return length * height * depth;
        }
 
        static void Main(string[] args)
        {
            var thisInstance = new OverloadExample();
 
            // invoking the first overload
            Console.WriteLine(String.Format("The yellow area is {0}.\n",
                thisInstance.DoCalculation(5, 10)));
 
            // invoking the second overload
            Console.WriteLine(String.Format("The volume of the shape is {0}.\n",
                thisInstance.DoCalculation(5, 10, 7)));
 
            Console.WriteLine("Hit any key to exit...");
            Console.ReadLine();
        }
    }
