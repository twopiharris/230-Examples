class TestRandom{
  public static void main(String[] args){
    int min = 0;
    int max = 100;
    
    for (int i = 0; i < 100; i++){
      int myNum = min + (int)(Math.random() * max-min + 1);
      System.out.println(myNum);
    }
  }
}