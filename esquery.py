'''
Created on Aug 26, 2015

@author: hazimhanif
'''
import requests
import re
import json

from elasticsearch import Elasticsearch
from pydoc import doc, Doc
es = Elasticsearch([{'host':'localhost' , 'port':'9200'}],send_get_body_as='POST')


def top_10_destination_country():
                
            res = es.search(index="fortigate(sf)-*",size=10,  body={
    
                    "size":0,
              "query": {
                "query_string": {
                  "analyze_wildcard": "true",
                  "query": "NOT dstip:192.168.* AND NOT dstip:10.* AND NOT dstip:[172.16.* TO 172.31.*]"
                }
              },     
                "aggs" : {
                "total":{
                    "date_range": {
                            "field": "@timestamp",
                            "ranges": [
                                {
                                "from": "now-24h" , 
                                "to": "now" 
                                }
                            ]
                     },
                    "aggs":{
                         "results" : {
                        "terms" : {
                            "field" : "geoip_dst.country_name.raw",
                            "size" : 10
                        }
                        }
                    }
            }
            }
    
                                                                               }
                                                                               )
                     
            msg=""
            msg = msg+"Displaying Top 10 Destination Country(24 hours):-"
            i=1
            for doc in res['aggregations']['total']['buckets'][0]['results']['buckets']:
                    st ='%d- %s -> (%s)' % (i,doc['key'], doc['doc_count'])
                    msg = msg + "\n \n" + st
                    i=i+1

            return msg
        
def top_10_destination_ip():
                
            res = es.search(index="fortigate(sf)-*",size=10,  body={
    
                    "size":0,
              "query": {
                "query_string": {
                  "analyze_wildcard": "true",
                  "query": "NOT dstip:192.168.* AND NOT dstip:10.* AND NOT dstip:[172.16.* TO 172.31.*]"
                }
              },     
                "aggs" : {
                "total":{
                    "date_range": {
                            "field": "@timestamp",
                            "ranges": [
                                {
                                "from": "now-24h" , 
                                "to": "now" 
                                }
                            ]
                     },
                    "aggs":{
                         "results" : {
                        "terms" : {
                            "field" : "dstip.raw",
                            "size" : 10
                        }
                        }
                    }
            }
            }
    
                                                                               }
                                                                               )
                     
            msg=""
            msg = msg+"Displaying Top 10 Destination IP(Last 24 hours):-"
            i=1
            for doc in res['aggregations']['total']['buckets'][0]['results']['buckets']:
                    st ='%d- %s -> (%s)' % (i,doc['key'], doc['doc_count'])
                    msg = msg + "\n \n" + st
                    i=i+1

            return msg     

def top_10_source_country():
                
            res = es.search(index="fortigate(sf)-*",size=10,  body={
    
                    "size":0,
              "query": {
                "query_string": {
                  "analyze_wildcard": "true",
                  "query": "NOT dstip:192.168.* AND NOT dstip:10.* AND NOT dstip:[172.16.* TO 172.31.*]"
                }
              },     
                "aggs" : {
                "total":{
                    "date_range": {
                            "field": "@timestamp",
                            "ranges": [
                                {
                                "from": "now-24h" , 
                                "to": "now" 
                                }
                            ]
                     },
                    "aggs":{
                         "results" : {
                        "terms" : {
                            "field" : "geoip_src.country_name.raw",
                            "size" : 10
                        }
                        }
                    }
            }
            }
    
                                                                               }
                                                                               )
                     
            msg=""
            msg = msg+"Displaying Top 10 Source Country(Last 24 hours):-"
            i=1
            for doc in res['aggregations']['total']['buckets'][0]['results']['buckets']:
                    st ='%d- %s -> (%s)' % (i,doc['key'], doc['doc_count'])
                    msg = msg + "\n \n" + st
                    i=i+1

            return msg

def top_10_source_ip():
                
            res = es.search(index="fortigate(sf)-*",size=10,  body={
    
                    "size":0,
              "query": {
                "query_string": {
                  "analyze_wildcard": "true",
                  "query": "NOT dstip:192.168.* AND NOT dstip:10.* AND NOT dstip:[172.16.* TO 172.31.*]"
                }
              },     
                "aggs" : {
                "total":{
                    "date_range": {
                            "field": "@timestamp",
                            "ranges": [
                                {
                                "from": "now-24h" , 
                                "to": "now" 
                                }
                            ]
                     },
                    "aggs":{
                         "results" : {
                        "terms" : {
                            "field" : "srcip.raw",
                            "size" : 10
                        }
                        }
                    }
            }
            }
    
                                                                               }
                                                                               )
                     
            msg=""
            msg = msg+"Displaying Top 10 Source IP(Last 24 hours):-"
            i=1
            for doc in res['aggregations']['total']['buckets'][0]['results']['buckets']:
                    st ='%d- %s -> (%s)' % (i,doc['key'], doc['doc_count'])
                    msg = msg + "\n \n" + st
                    i=i+1

            return msg      

def top_10_status():
                
            res = es.search(index="fortigate(sf)-*",size=10,  body={
    
                    "size":0,
              "query": {
                "query_string": {
                  "analyze_wildcard": "true",
                  "query": "NOT dstip:192.168.* AND NOT dstip:10.* AND NOT dstip:[172.16.* TO 172.31.*]"
                }
              },     
                "aggs" : {
                "total":{
                    "date_range": {
                            "field": "@timestamp",
                            "ranges": [
                                {
                                "from": "now-24h" , 
                                "to": "now" 
                                }
                            ]
                     },
                    "aggs":{
                         "results" : {
                        "terms" : {
                            "field" : "status.raw",
                            "size" : 10
                        }
                        }
                    }
            }
            }
    
                                                                               }
                                                                               )
                     
            msg=""
            msg = msg+"Displaying Top 10 Status(Last 24 hours):-"
            i=1
            for doc in res['aggregations']['total']['buckets'][0]['results']['buckets']:
                    st ='%d- %s -> (%s)' % (i,doc['key'], doc['doc_count'])
                    msg = msg + "\n \n" + st
                    i=i+1

            return msg    

def top_10_level():
                
            res = es.search(index="fortigate(sf)-*",size=10,  body={
    
                    "size":0,
              "query": {
                "query_string": {
                  "analyze_wildcard": "true",
                  "query": "NOT dstip:192.168.* AND NOT dstip:10.* AND NOT dstip:[172.16.* TO 172.31.*]"
                }
              },     
                "aggs" : {
                "total":{
                    "date_range": {
                            "field": "@timestamp",
                            "ranges": [
                                {
                                "from": "now-24h" , 
                                "to": "now" 
                                }
                            ]
                     },
                    "aggs":{
                         "results" : {
                        "terms" : {
                            "field" : "level.raw",
                            "size" : 10
                        }
                        }
                    }
            }
            }
    
                                                                               }
                                                                               )
                     
            msg=""
            msg = msg+"Displaying Top 10 Level(Last 24 hours):-"
            i=1
            for doc in res['aggregations']['total']['buckets'][0]['results']['buckets']:
                    st ='%d- %s -> (%s)' % (i,doc['key'], doc['doc_count'])
                    msg = msg + "\n \n" + st
                    i=i+1

            return msg

def top_10_reason():
                
            res = es.search(index="fortigate(sf)-*",size=10,  body={
    
                    "size":0,
              "query": {
                "query_string": {
                  "analyze_wildcard": "true",
                  "query": "NOT dstip:192.168.* AND NOT dstip:10.* AND NOT dstip:[172.16.* TO 172.31.*]"
                }
              },     
                "aggs" : {
                "total":{
                    "date_range": {
                            "field": "@timestamp",
                            "ranges": [
                                {
                                "from": "now-24h" , 
                                "to": "now" 
                                }
                            ]
                     },
                    "aggs":{
                         "results" : {
                        "terms" : {
                            "field" : "reason.raw",
                            "size" : 10
                        }
                        }
                    }
            }
            }
    
                                                                               }
                                                                               )
                     
            msg=""
            msg = msg+"Displaying Top 10 Reason(Last 24 hours):-"
            i=1
            for doc in res['aggregations']['total']['buckets'][0]['results']['buckets']:
                    st ='%d- %s -> (%s)' % (i,doc['key'], doc['doc_count'])
                    msg = msg + "\n \n" + st
                    i=i+1

            return msg
        
def top_10_message():
                
            res = es.search(index="fortigate(sf)-*",size=10,  body={
    
                    "size":0,
              "query": {
                "query_string": {
                  "analyze_wildcard": "true",
                  "query": "NOT dstip:192.168.* AND NOT dstip:10.* AND NOT dstip:[172.16.* TO 172.31.*]"
                }
              },     
                "aggs" : {
                "total":{
                    "date_range": {
                            "field": "@timestamp",
                            "ranges": [
                                {
                                "from": "now-24h" , 
                                "to": "now" 
                                }
                            ]
                     },
                    "aggs":{
                         "results" : {
                        "terms" : {
                            "field" : "msg.raw",
                            "size" : 10
                        }
                        }
                    }
            }
            }
    
                                                                               }
                                                                               )
                     
            msg=""
            msg = msg+"Displaying Top 10 Message(Last 24 hours):-"
            i=1
            for doc in res['aggregations']['total']['buckets'][0]['results']['buckets']:
                    st ='%d- %s -> (%s)' % (i,doc['key'], doc['doc_count'])
                    msg = msg + "\n \n" + st
                    i=i+1

            return msg
                     
                