/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.assignment.fillinstation.model;

import java.io.File;
import java.io.IOException;
import java.net.URISyntaxException;
import java.util.List;
import org.apache.commons.io.FileUtils;

/**
 *
 * @author DangThanh
 */
public class Dictionary {

    private File dictionaryFile;
    private List<String> dictionary;
    private static Dictionary instance = null;
    
    private Dictionary() throws URISyntaxException, IOException {
        this.dictionaryFile = new File(Dictionary.class.getClassLoader().getResource("3_letters_dictionary").toURI());
        this.loadDictionary();
    }
    
    public static void initDictionary() throws URISyntaxException, IOException {
        if(instance == null) {
            instance = new Dictionary();
        }
    }

    public static Dictionary getDictionary() throws Exception {
        if(instance == null) {
            throw new Exception("Dictionary is null");
        }
        return instance;
    }
    
    private void loadDictionary() throws IOException {
        this.dictionary = FileUtils.readLines(dictionaryFile);
    }

    public boolean isContain(Word word) {
        return this.dictionary.contains(word.toString());
    }
}
