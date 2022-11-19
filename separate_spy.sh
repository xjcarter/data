#!/bin/bash

header='Date,Open,High,Low,Close,Adj Close,Volume'
yrs='2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022'
for yr in $yrs
do
    tag="SPY_${yr}".csv
    echo $tag
    echo $header >$tag
    cat SPY.csv | grep "${yr}-" >>$tag
    head -5 $tag
    tail -5 $tag
done
