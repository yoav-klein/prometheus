#!/bin/bash


function delay() {
    ms=$1
    curl prom-lab/latency/$ms
}

function cycle() {
    num=$1
    delay=$2

    for i in $(seq 1 $num); do
        delay $delay
    done
}


function scenario_a() {
    cycle 50 2
    cycle 100 6
    cycle 30 20
    cycle 30 80
    cycle 10 200
    cycle 4 500
    cycle 2 1350
}


function run_once() {
    scenario_a
}

function run_constant() {
    while $true; do
        run_once
    done
}

run_once
