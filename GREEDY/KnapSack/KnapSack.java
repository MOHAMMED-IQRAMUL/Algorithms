import java.util.*;

public class KnapSack {

    public static double KnapSack_Greedy(List<double[]> WP, double MaxWeight) {

        double TotalValue = 0;
        double TotalWeight = 0;
        Collections.sort(WP, new Comparator<double[]>() {
            @Override
            public int compare(double[] a, double[] b) {
                double ratioA =  a[1] / a[0];
                double ratioB =  b[1] / b[0];
                return Double.compare(ratioB, ratioA);
            }
        });
        for (int i = 0; i < WP.size(); i++) {
            if (TotalWeight + WP.get(i)[0] <= MaxWeight) {
                TotalValue += WP.get(i)[1];
                TotalWeight += WP.get(i)[0];
            } else {
                TotalValue += (MaxWeight - TotalWeight) * (WP.get(i)[1] / WP.get(i)[0]);
                TotalWeight = MaxWeight;
                break;
            }
        }
        return TotalValue;
    }

    public static void main(String[] args) {
        List<double[]> Arr1 = new ArrayList<>();
        Arr1.add(new double[] { 2, 10 });
        Arr1.add(new double[] { 1, 5 });
        Arr1.add(new double[] { 3, 15 });
        Arr1.add(new double[] { 4, 20 });
        double MaxWeight = 5;
        System.out.println(KnapSack_Greedy(Arr1, MaxWeight));

        List<double[]> Arr2 = new ArrayList<>();
        Arr2.add(new double[] { 5, 30 });
        Arr2.add(new double[] { 10, 40 });
        Arr2.add(new double[] { 15, 45 });
        Arr2.add(new double[] { 22, 77 });
        Arr2.add(new double[] { 25, 90 });
        MaxWeight = 60;
        System.out.println(KnapSack_Greedy(Arr2, MaxWeight));

        List<double[]> Arr3 = new ArrayList<>();
        Arr3.add(new double[] { 40, 280 });
        Arr3.add(new double[] { 10, 100 });
        Arr3.add(new double[] { 20, 120 });
        Arr3.add(new double[] { 24, 120 });
        MaxWeight = 60;
        System.out.println(KnapSack_Greedy(Arr3, MaxWeight));
    }
}