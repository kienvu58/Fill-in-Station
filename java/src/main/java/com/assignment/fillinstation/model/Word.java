/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.assignment.fillinstation.model;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author DangThanh
 */
public class Word {
    private List<String> letter;
    
    public Word(List<String> letter) {
        this.letter = new ArrayList<>();
    }
    
    public void updateWord(String letter, int index) {
        if(letter.length() == 3) {
            this.letter.set(index, letter);
            return;
        }
        this.letter.add(letter);
    }
    
    public List<String> getWord() {
        return this.letter;
    }

    @Override
    public String toString() {
        StringBuilder word = new StringBuilder();
        for (String let : letter) {
            word.append(let);
        }
        return word.toString();
    }
}
