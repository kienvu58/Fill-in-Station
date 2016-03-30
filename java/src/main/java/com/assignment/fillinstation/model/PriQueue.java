/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.assignment.fillinstation.model;

import com.assignment.fillinstation.FillinStationProblem.State;
import com.assignment.fillinstation.model.PriQueue.Item;
import java.util.Comparator;
import java.util.PriorityQueue;

/**
 *
 * @author DangThanh
 */
public class PriQueue<T> {

    private PriorityQueue<Item> priorityQueue;
    private Comparator comparator = new Comparator() {
        @Override
        public int compare(Object o1, Object o2) {
            if (((Item) o2).getPriority() < ((Item) o1).getPriority()) {
                return -1;
            }
            return 1;
        }
    };

    public PriQueue() {
        this.priorityQueue = new PriorityQueue<Item>(comparator);
    }

    public void push(T item, double priority) {
        Item object = new PriQueue.Item(item, priority);
        this.priorityQueue.add(object);
    }

    public T pop() {
        return this.priorityQueue.poll().getContent();
    }

    public int size() {
        return this.priorityQueue.size();
    }

    public boolean isEmpty() {
        return this.priorityQueue.isEmpty();
    }

    public class Item {

        private T content;
        private double priority;

        public Item(T state, double priority) {
            this.content = state;
            this.priority = priority;
        }

        public T getContent() {
            return content;
        }

        public double getPriority() {
            return priority;
        }
    }
}
