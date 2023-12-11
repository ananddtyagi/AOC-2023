import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Map.Entry;

class Part2 {

    // class Node {
    //     String value;
    //     Node left;
    //     Node right;

    //     Node(String value){
    //         this.value = value;
    //     }

    //     void setLeftNode(Node left) {
    //         this.left = left;
    //     }

    //     void setRightNode(Node right) {
    //         this.right = right;
    //     }
    // /**
    //  * @param args
    //  */
    // }

    public static void main(String[] args) {
        try {
            File fileObj = new File("data.txt");
            Scanner scanner = new Scanner(fileObj);
            HashMap<String, String[]> graph = new HashMap<>();

            String instructions = scanner.nextLine();
            scanner.nextLine();
            while(scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String node_val = line.substring(0,3);
                String left = line.substring(7,10);
                String right = line.substring(12,15);
                String[] lr = {left, right};
                graph.put(node_val, lr);
            }
            
            ArrayList<String> startNodes = new ArrayList<>();

            for(Entry<String, String[]> entry : graph.entrySet()) {
                    String key = entry.getKey();
                    if (key.charAt(2) == 'A'){
                        startNodes.add(key);
                    }
            }
            int count = getFinishCount(graph, instructions, startNodes);
            System.out.println(count);
        } catch(FileNotFoundException e){
        } 
    }

    static boolean allEndInZ(List<String> nodes) {
        for (String node: nodes) {
            if (!(node.charAt(2) == 'Z')) {
                return false;
            }
        }
        return true;
    }

    private static int getFinishCount(HashMap<String, String[]> graph, String instructions, ArrayList<String> currNodes) {
        int count = 0;
        Character instruction;
        int instruction_len = instructions.length();
        // System.out.println(currNodes);
        while(!allEndInZ(currNodes)) {
            instruction = instructions.charAt(count % instruction_len);
            // System.out.println(instruction);
            for (int i = 0; i < currNodes.size(); i++) {
                if (instruction == 'L') {
                    currNodes.set(i, graph.get(currNodes.get(i))[0]);
                } else {
                    currNodes.set(i, graph.get(currNodes.get(i))[1]);
                }
            }
            // System.out.println(currNodes);
            count++;
        }
        return count;
    }
}