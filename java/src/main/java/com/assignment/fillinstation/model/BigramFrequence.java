/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.assignment.fillinstation.model;

import java.io.File;
import java.io.IOException;
import java.net.URISyntaxException;
import java.util.ArrayList;
import java.util.List;
import org.apache.commons.io.FileUtils;

/**
 *
 * @author DangThanh
 */
public class BigramFrequence {

    private List<Bigram> bigramFrequenceList;
    private File bigramFile;
    private static BigramFrequence instance;
    
    public static void init() throws URISyntaxException, IOException {
        if(instance == null) {
            instance = new BigramFrequence();
        }
    }
    
    public static BigramFrequence getInstance() throws Exception {
        if(instance == null) {
            throw new Exception("Bigram is null");
        }
        return instance;
    }
    
    private BigramFrequence() throws URISyntaxException, IOException {
        this.bigramFile = new File(BigramFrequence.class.getClassLoader().getResource("bigram_frequence_list").toURI());
        this.bigramFrequenceList = new ArrayList<>();
        this.loadData();
    }

    private void loadData() throws IOException {
        List<String> dataList = FileUtils.readLines(bigramFile);
        for (String data : dataList) {
            String[] split = data.split(" ");
            bigramFrequenceList.add(new Bigram(split[0], split[1], Double.parseDouble(split[2])));
        }
    }

    public double getFrequence(String firstLetter, String secondLetter) {
        Bigram bigram = new Bigram(firstLetter, secondLetter, 0);
        for (Bigram lBigram : bigramFrequenceList) {
            if(lBigram.equals(bigram)) {
                return lBigram.getFrequence();
            }
        }
        return 0;
    }
    
    public class Bigram {

        private String firstLetter;
        private String secondLetter;
        private double frequence;

        public Bigram(String firstLetter, String secondLetter, double frequence) {
            this.firstLetter = firstLetter;
            this.secondLetter = secondLetter;
            this.frequence = frequence;
        }

        public String getFirstLetter() {
            return firstLetter;
        }

        public String getSecondLetter() {
            return secondLetter;
        }

        public double getFrequence() {
            return frequence;
        }

        @Override
        public boolean equals(Object obj) {
            Bigram bigram = (Bigram)obj;
            boolean cond1 = bigram.getFirstLetter().equalsIgnoreCase(firstLetter);
            boolean cond2 = bigram.getSecondLetter().equalsIgnoreCase(secondLetter);
            return cond1 && cond2;
        }
    }
}
