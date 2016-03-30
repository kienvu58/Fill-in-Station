/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.assignment.fillinstation;

import com.assignment.fillinstation.model.MatrixIndex;
import com.assignment.fillinstation.model.Dictionary;
import com.assignment.fillinstation.model.Word;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 *
 * @author DangThanh
 */
public class FillinStationProblem {

    private static final List<List<Integer>> constraints = new ArrayList<>();
    
    private static void initContraints() {
        constraints.add(Arrays.asList(00, 01, 02));
        constraints.add(Arrays.asList(00, 10, 20));
        constraints.add(Arrays.asList(01, 11, 21));
        constraints.add(Arrays.asList(02, 12, 22));
        constraints.add(Arrays.asList(10, 11, 12));
        constraints.add(Arrays.asList(20, 21, 22));
        constraints.add(Arrays.asList(00, 11, 22));
        constraints.add(Arrays.asList(02, 11, 20));
    }

    public FillinStationProblem() {
        try {
            Dictionary.initDictionary();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
        this.initContraints();
    }

    //=> Kiem tra cac rang buoc
    public boolean checkContraints(State state) {
        for (List<Integer> constraint : constraints) {
            Word word = new Word(Collections.EMPTY_LIST);
            for (int i = 0; i < 3; i++) {
                int row = constraint.get(i) / 10;
                int col = constraint.get(i) % 10;
                String letter = state.getLetter(new MatrixIndex(row, col));
                if (letter.equals("*")) {
                    continue;
                }
                word.updateWord(letter, i);
            }
            try {
                if (word.getWord().size() == 3 && !Dictionary.getDictionary().isContain(word)) {
                    return false;
                }
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
        return true;
    }

    //=> Kiem tra Trang thai ket thuc
    public boolean isGoalState(State state) {
        return state.isFullState() && this.checkContraints(state);
    }

    public static class State {

        private final int MAX_ROW = 3;
        private final int MAX_COL = 3;
        private String[][] state = new String[MAX_ROW][MAX_COL];
        private MatrixIndex currentIndex;

        public State() {
            this.currentIndex = new MatrixIndex(0, -1);
        }

        public State clone() {
            State cloneState = new State();
            for (int row = 0; row < MAX_ROW; row++) {
                for (int col = 0; col < MAX_COL; col++) {
                    cloneState.state[row][col] = this.state[row][col];
                }
            }
            cloneState.currentIndex = new MatrixIndex(this.currentIndex.getRow(), this.currentIndex.getColumn());
            return cloneState;
        }

        public void pushToState(String letter, MatrixIndex index) {
            this.state[index.getRow()][index.getColumn()] = letter;
            this.currentIndex = index;
        }

        public String getLetter(MatrixIndex index) {
            if (index.getRow() < 0 || index.getColumn() < 0) {
                return "$";
            }
            String letter = state[index.getRow()][index.getColumn()];
            return letter != null ? letter : "*";
        }

        public MatrixIndex getNextIndex(MatrixIndex curIndex, Direction direction) {
            switch (direction) {
                case MAIN_DIAGONAL:
                    if (curIndex.getRow() < MAX_ROW - 1 && curIndex.getColumn() < MAX_COL - 1) {
                        return new MatrixIndex(curIndex.getRow() + 1, curIndex.getColumn() + 1);
                    }
                    break;
                case ANTI_DIAGONAL:
                    if (curIndex.getRow() < MAX_ROW - 1) {
                        return new MatrixIndex(curIndex.getRow() + 1, curIndex.getColumn() - 1);
                    }
                    break;
                case HORIZONTAL: //=> Hang ngang
                    if (curIndex.getColumn() < MAX_COL - 1) {
                        return new MatrixIndex(curIndex.getRow(), curIndex.getColumn() + 1);
                    }
                    return new MatrixIndex(curIndex.getRow() + 1, 0);
                case VERTICAL:
                    if (curIndex.getRow() < MAX_ROW - 1) {
                        return new MatrixIndex(curIndex.getRow() + 1, curIndex.getColumn());
                    }
                    return new MatrixIndex(0, curIndex.getColumn() + 1);
            }
            return null;
        }

        public MatrixIndex getPrevIndex(MatrixIndex curIndex, Direction direction) {
            switch (direction) {
                case MAIN_DIAGONAL:
                    if (curIndex.getRow() > 0 && curIndex.getColumn() > 0) {
                        return new MatrixIndex(curIndex.getRow() - 1, curIndex.getColumn() - 1);
                    }
                    break;
                case ANTI_DIAGONAL:
                    if (curIndex.getRow() > 0) {
                        return new MatrixIndex(curIndex.getRow() - 1, curIndex.getColumn() + 1);
                    }
                    break;
                case HORIZONTAL:
                    if (curIndex.getColumn() > 0) {
                        return new MatrixIndex(curIndex.getRow(), curIndex.getColumn() - 1);
                    }
                    return new MatrixIndex(curIndex.getRow() - 1, MAX_COL - 1);
                case VERTICAL:
                    if (curIndex.getRow() > 0) {
                        return new MatrixIndex(curIndex.getRow() - 1, curIndex.getColumn());
                    }
                    return new MatrixIndex(MAX_ROW - 1, curIndex.getColumn() - 1);
            }
            return null;
        }

        private boolean isFullState() {
            for (int row = 0; row < 3; row++) {
                for (int col = 0; col < 3; col++) {
                    if (this.getLetter(new MatrixIndex(row, col)).equals("*")) {
                        return false;
                    }
                }
            }
            return true;
        }

        public MatrixIndex getCurrentIndex() {
            return this.currentIndex;
        }

        public String[][] getState() {
            return state;
        }
    }

    public enum Direction {

        VERTICAL,
        HORIZONTAL,
        MAIN_DIAGONAL,
        ANTI_DIAGONAL
    }
}
