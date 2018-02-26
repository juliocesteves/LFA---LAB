/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aula01;

import java.util.regex.Pattern;
import javax.swing.JOptionPane;

/**
 *
 * @author 145052
 */
public class Aula01 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        String palavra = JOptionPane.showInputDialog("Digite a Palavra");

        if (ValidaEx1(palavra)) {
            System.out.println("Palavra Existe");
        } else {
            System.out.println("Palavra Não Existe");
        }
    }

    public static boolean ValidaEx1(String input) {
        String S = "AA";
        String aux = "";
        int countA, countB;
        int troca = 0, insertAfter = 0;
        boolean valida = false;
        int tam = input.length();
        
        while(S.length() <= tam - 1) {
            //S = S.replace("A", "aB");
            if (existeMaiuscula(S)) {
                insertAfter++;
                S = S.replaceFirst(Pattern.quote("A"), "aB");
                troca++;
                aux = validaExpressao(S, input, troca);
                if (!aux.isEmpty()) {
                    S = aux;
                    insertAfter++;
                    continue;
                }
                
                troca = 0;
                aux = "";
                S = S.replace("aB", "Ba");
                insertAfter++;
                troca++;
                aux = validaExpressao(S, input, troca);
                if (!aux.isEmpty()) {
                    S = aux;
                    insertAfter++;
                }
            } else {
                S = S + Character.toString(input.charAt(insertAfter));
            }
        }
        
        if (S.equals(input)){
            valida = true;
        }
        
        countA = S.length() - S.replace("a", "").length();
        countB = S.length() - S.replace("b", "").length();

        return (valida && countA == 2 && countB >= 2);
    }

    public static boolean ValidaEx2(String input) {
        String S = "A0";
        boolean valida = false;
        int tam = input.length();

        while (S.length() <= tam - 1) {
            S = S.replace("A", "A0");
            if (validaFinal(S, input)) {
                if (S.length() == tam) {
                    valida = true;
                    break;
                }
                continue; //Mantém a mesma lógica caso esteja certo o match da palavra
            }
            
            S = S.replace("A0", "A1");
            if (validaFinal(S, input)) {
                if (S.length() == tam) {
                    valida = true;
                    break;
                }
                continue;
            }
        }
        return valida;
    }

    public static boolean validaFinal(String gramatica, String input) {
        String aux = gramatica;
        aux = aux.replace("A", "0");
        if (aux.equals(input) || (input.indexOf(aux, 
                                  input.length() - aux.length()) != -1)) {
            return true;
        } else {
            aux = gramatica;
            aux = aux.replace("A", "1");
            if (aux.equals(input) || (input.indexOf(aux, 
                                  input.length() - aux.length()) != -1)) {
                return true;
            }
        }

        return false;
    }
    
    public static String validaExpressao(String gramatica, String input, int troca) {
        String aux = gramatica;
        
        aux = aux.replace("B", "b");
        if (aux.equals(input) || aux.substring(0, troca+1).equals(input.substring(0, troca+1))) {
            return aux;
        } else {
            aux = gramatica;
            aux = aux.replace("B", "Ba");
            
        }
        return "";
    }
    
    private static boolean existeMaiuscula(String input) {
        String aux = String.valueOf(input);
        
        boolean maiuscula = !aux.equals(aux.toLowerCase());
        
        return maiuscula;
    }   
}

