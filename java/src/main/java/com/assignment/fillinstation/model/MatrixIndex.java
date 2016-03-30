/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.assignment.fillinstation.model;

/**
 *
 * @author DangThanh
 */
public class MatrixIndex {

   private int row;
   private int column;
   
   public MatrixIndex(int row, int column) {
       this.column = column;
       this.row = row;
   }
   
   public int getRow() {
       return this.row;
   }
   
   public int getColumn() {
       return this.column;
   }
}
