/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.assignment.fillinstation;

import com.assignment.fillinstation.model.MatrixIndex;
import com.assignment.fillinstation.model.Dictionary;
import com.assignment.fillinstation.model.PriQueue;
import com.assignment.fillinstation.model.BigramFrequence;
import com.assignment.fillinstation.FillinStationProblem.Direction;
import com.assignment.fillinstation.FillinStationProblem.State;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 *
 * @author DangThanh
 */
public class SearchAlgorithm {

    private Dictionary dictionary;
    private BigramFrequence bigramFrequence;
    private List<String> domain = Arrays.asList();
    private int nodeCounter = 0;
    private FillinStationProblem problem;

    public SearchAlgorithm(List<String> input) throws Exception {
        Dictionary.initDictionary();
        BigramFrequence.init();
        this.dictionary = Dictionary.getDictionary();
        this.bigramFrequence = BigramFrequence.getInstance();
        this.problem = new FillinStationProblem();
        this.domain = input;
    }

    private PriQueue getSuccessor(State currentState) {
        PriQueue queue = new PriQueue();
        List<String> currentDomain = this.getCurrentDomain(currentState);
        for (String letter : currentDomain) {
            MatrixIndex nextIndex = this.chooseNextIndex(currentState);
            double heuristic = this.advancedHeuristic(currentState, letter);
//            double heuristic = this.normalHeuristic(currentState, letter);
            if (heuristic == 0) {
                continue;
            }
            State nextState = currentState.clone();
            nextState.pushToState(letter, nextIndex);
            if (this.problem.checkContraints(nextState)) {
                queue.push(nextState, heuristic);
                this.nodeCounter++;
            }
        }
        return queue;
    }

    //=> Solve Problem
    public State solve(State currentState) {
        if (this.problem.isGoalState(currentState)) {
            return currentState;
        } else {
            PriQueue successor = this.getSuccessor(currentState);
            while (!successor.isEmpty()) {
                State nextState = (State) successor.pop();
                State result = this.solve(nextState);
                if (result != null) {
                    //Resturn Success State
                    return result;
                }
            }
        }
        return null;
    }

    private MatrixIndex chooseNextIndex(State state) {
        return state.getNextIndex(state.getCurrentIndex(), Direction.HORIZONTAL);
    }

    private List<String> getCurrentDomain(State state) {
        List<String> curDomain = new ArrayList();
        for (String letter : this.domain) {
            curDomain.add(letter);
        }
        for (int row = 0; row < 3; row++) {
            for (int col = 0; col < 3; col++) {
                String letter = state.getLetter(new MatrixIndex(row, col));
                curDomain.remove(letter);
            }
        }
        return curDomain;
    }

    //=> Normal Heuristic
    private double normalHeuristic(State curState, String nextLetter) {
        MatrixIndex nextIndex = curState.getNextIndex(curState.getCurrentIndex(), Direction.HORIZONTAL);
        if (nextIndex.getRow() == 0 || nextIndex.getColumn() == 0) {
            return this.bigramFrequence.getFrequence("$", nextLetter);
        }
        String curLetter = curState.getLetter(curState.getCurrentIndex());
        return this.bigramFrequence.getFrequence(curLetter, nextLetter);
    }

    //=> Advanced Heuristic
    private double advancedHeuristic(State curState, String nextLetter) {
        MatrixIndex nextIndex = curState.getNextIndex(curState.getCurrentIndex(), Direction.HORIZONTAL);
        int nextRow = nextIndex.getRow();
        int nextCol = nextIndex.getColumn();
        double heuristic = 1;

        if (nextCol == 0 || nextRow == 0) {
            heuristic *= this.bigramFrequence.getFrequence("$", nextLetter);
        }

        //=> Horizontal
        if (nextCol > 0) {
            MatrixIndex prevIndex = curState.getPrevIndex(nextIndex, Direction.HORIZONTAL);
            String curLetter = curState.getLetter(prevIndex);
            heuristic *= this.bigramFrequence.getFrequence(curLetter, nextLetter);
            //=> Main Diagonal
            if (nextRow == nextCol) {
                prevIndex = curState.getPrevIndex(nextIndex, Direction.MAIN_DIAGONAL);
                curLetter = curState.getLetter(prevIndex);
                heuristic *= this.bigramFrequence.getFrequence(curLetter, nextLetter);
            }
        }

        if (nextRow > 0) {
            //=> Vertical
            MatrixIndex prevIndex = curState.getPrevIndex(nextIndex, Direction.VERTICAL);
            String curLetter = curState.getLetter(prevIndex);
            heuristic *= this.bigramFrequence.getFrequence(curLetter, nextLetter);
            
            //=> Anti Diagonal
            if (nextCol == (2 - nextRow)) {
                prevIndex = curState.getPrevIndex(nextIndex, Direction.ANTI_DIAGONAL);
                curLetter = curState.getLetter(prevIndex);
                heuristic *= this.bigramFrequence.getFrequence(curLetter, nextLetter);
            }
        }
        return heuristic;
    }

    public void printSolution(State successState) {
        for (int row = 0; row < 3; row++) {
            for (int col = 0; col < 3; col++) {
                System.out.print(successState.getLetter(new MatrixIndex(row, col)) + " ");
            }
            System.out.println("");
        }
        System.out.println(this.nodeCounter + " Node expanded!");
    }

    public static void main(String[] args) throws Exception {
        FillinStationProblem.State state = new State();
        List<String> input1 = new ArrayList<String>(Arrays.asList("A", "E", "O",
                "P", "R", "R",
                "S", "W", "Y"));
        List<String> input2 = new ArrayList<String>(Arrays.asList("A", "E", "E",
                "I", "K", "L",
                "L", "P", "Y"));
        try {
            SearchAlgorithm searchAlgorithm = new SearchAlgorithm(input1);
            State solution = searchAlgorithm.solve(state);
            if (solution != null) {
                searchAlgorithm.printSolution(solution);
            } else {
                System.out.println("Khong tim thay ket qua");
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}
