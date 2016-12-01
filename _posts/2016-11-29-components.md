---
layout: post
title: Components
---

## Annotations

Our news consumers' manual will be delivered by way of annotations using [Hypothes.is](https://hypothes.is). These annotations can be generated using the three mechanisms below. 

The annotations can be displayed by including code in the publishing website - this can be a signal of a publisher willing to deal with critical consumers - or by activating a browser plugin, making available the annotations to consumers without the publishers consent. 

The annotations can be queried using hypothes.is' API, making them available as signals for search engines. 


## Citations Ex-Ray

Portmanteau word of "Expert" and "X-Ray" - we will return a sample of citations of quoted named entites, meant to give a flavour of what kind of citations an expert
gets quoted with.

<script language="mermaid">
graph TB 
            i(Citation Index) --> a(Annotations)
            Text-->t
            Text-->p
			t(NER)  --> c(Cited NE)
			p(POS Tagger) --> c
            c-->a
            
            
</script>

## Out-of-Bubble Recommendation

By manually classifying available sources, we can give "the other perspective" by recommending news with similar named entities from other source groups.

<script language="mermaid">
graph TB 
            t(Text)-->n
			n(TXTWerk NERD)  --> i(Juicer Query)
            t-->f(Source Group Classificator)
            f-->i
            i-->a(Annotations)
            
</script>

## Language hints

By manually classifying available sources, we can give "the other perspective" if we recommend news with similar named entities from other source groups than the one the current text belongs to.

<script language="mermaid">
graph TB 
            t(Text)-->p
            p(Signal Phrases)-->n
            n(Annotations)
            
</script>
