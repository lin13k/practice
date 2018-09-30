/**
 * The rand7() API is already defined in the parent class SolBase.
 * public int rand7();
 * @return a random integer in the range 1 to 7
 */
class Solution extends SolBase {
    public int rand10() {
    	int idx = 0;
        do {
        	idx = rand7() + (rand7() - 1) * 7;
        }while (idx > 40);
        return (idx%10) + 1;
    }
}