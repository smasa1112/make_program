/* ----------------------------------------------------------------- */
/*           The Japanese TTS System "Open JTalk"                    */
/*           developed by HTS Working Group                          */
/*           http://open-jtalk.sourceforge.net/                      */
/* ----------------------------------------------------------------- */
/*                                                                   */
/*  Copyright (c) 2008-2016  Nagoya Institute of Technology          */
/*                           Department of Computer Science          */
/*                                                                   */
/* All rights reserved.                                              */
/*                                                                   */
/* Redistribution and use in source and binary forms, with or        */
/* without modification, are permitted provided that the following   */
/* conditions are met:                                               */
/*                                                                   */
/* - Redistributions of source code must retain the above copyright  */
/*   notice, this list of conditions and the following disclaimer.   */
/* - Redistributions in binary form must reproduce the above         */
/*   copyright notice, this list of conditions and the following     */
/*   disclaimer in the documentation and/or other materials provided */
/*   with the distribution.                                          */
/* - Neither the name of the HTS working group nor the names of its  */
/*   contributors may be used to endorse or promote products derived */
/*   from this software without specific prior written permission.   */
/*                                                                   */
/* THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND            */
/* CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,       */
/* INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF          */
/* MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE          */
/* DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS */
/* BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,          */
/* EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED   */
/* TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,     */
/* DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON */
/* ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,   */
/* OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY    */
/* OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE           */
/* POSSIBILITY OF SUCH DAMAGE.                                       */
/* ----------------------------------------------------------------- */

#ifndef NJD_SET_ACCENT_PHRASE_RULE_H
#define NJD_SET_ACCENT_PHRASE_RULE_H

#ifdef __cplusplus
#define NJD_SET_ACCENT_PHRASE_RULE_H_START extern "C" {
#define NJD_SET_ACCENT_PHRASE_RULE_H_END   }
#else
#define NJD_SET_ACCENT_PHRASE_RULE_H_START
#define NJD_SET_ACCENT_PHRASE_RULE_H_END
#endif                          /* __CPLUSPLUS */

NJD_SET_ACCENT_PHRASE_RULE_H_START;

/*
  Rule 01 \x83\x66\x83\x74\x83\x48\x83\x8b\x83\x67\x82\xcd\x82\xad\x82\xc1\x82\xc2\x82\xaf\x82\xe9
  Rule 02 \x81\x75\x96\xbc\x8e\x8c\x81\x76\x82\xcc\x98\x41\x91\xb1\x82\xcd\x82\xad\x82\xc1\x82\xc2\x82\xaf\x82\xe9
  Rule 03 \x81\x75\x8c\x60\x97\x65\x8e\x8c\x81\x76\x82\xcc\x8c\xe3\x82\xc9\x81\x75\x96\xbc\x8e\x8c\x81\x76\x82\xaa\x82\xab\x82\xbd\x82\xe7\x95\xca\x82\xcc\x83\x41\x83\x4e\x83\x5a\x83\x93\x83\x67\x8b\xe5\x82\xc9
  Rule 04 \x81\x75\x96\xbc\x8e\x8c,\x8c\x60\x97\x65\x93\xae\x8e\x8c\x8c\xea\x8a\xb2\x81\x76\x82\xcc\x8c\xe3\x82\xc9\x81\x75\x96\xbc\x8e\x8c\x81\x76\x82\xaa\x82\xab\x82\xbd\x82\xe7\x95\xca\x82\xcc\x83\x41\x83\x4e\x83\x5a\x83\x93\x83\x67\x8b\xe5\x82\xc9
  Rule 05 \x81\x75\x93\xae\x8e\x8c\x81\x76\x82\xcc\x8c\xe3\x82\xc9\x81\x75\x8c\x60\x97\x65\x8e\x8c\x81\x76or\x81\x75\x96\xbc\x8e\x8c\x81\x76\x82\xaa\x82\xab\x82\xbd\x82\xe7\x95\xca\x82\xcc\x83\x41\x83\x4e\x83\x5a\x83\x93\x83\x67\x8b\xe5\x82\xc9
  Rule 06 \x81\x75\x95\x9b\x8e\x8c\x81\x76\x81\x43\x81\x75\x90\xda\x91\xb1\x8e\x8c\x81\x76\x81\x43\x81\x75\x98\x41\x91\xcc\x8e\x8c\x81\x76\x82\xcd\x92\x50\x93\xc6\x82\xcc\x83\x41\x83\x4e\x83\x5a\x83\x93\x83\x67\x8b\xe5\x82\xc9
  Rule 07 \x81\x75\x96\xbc\x8e\x8c,\x95\x9b\x8e\x8c\x89\xc2\x94\x5c\x81\x76\x81\x69\x82\xb7\x82\xd7\x82\xc4\x81\x43\x82\xc8\x82\xc7\x81\x6a\x82\xcd\x92\x50\x93\xc6\x82\xcc\x83\x41\x83\x4e\x83\x5a\x83\x93\x83\x67\x8b\xe5\x82\xc9
  Rule 08 \x81\x75\x8f\x95\x8e\x8c\x81\x76or\x81\x75\x8f\x95\x93\xae\x8e\x8c\x81\x76\x81\x69\x95\x74\x91\xae\x8c\xea\x81\x6a\x82\xcd\x91\x4f\x82\xc9\x82\xad\x82\xc1\x82\xc2\x82\xaf\x82\xe9
  Rule 09 \x81\x75\x8f\x95\x8e\x8c\x81\x76or\x81\x75\x8f\x95\x93\xae\x8e\x8c\x81\x76\x81\x69\x95\x74\x91\xae\x8c\xea\x81\x6a\x82\xcc\x8c\xe3\x82\xcc\x81\x75\x8f\x95\x8e\x8c\x81\x76\x81\x43\x81\x75\x8f\x95\x93\xae\x8e\x8c\x81\x76\x88\xc8\x8a\x4f\x81\x69\x8e\xa9\x97\xa7\x8c\xea\x81\x6a\x82\xcd\x95\xca\x82\xcc\x83\x41\x83\x4e\x83\x5a\x83\x93\x83\x67\x8b\xe5\x82\xc9
  Rule 10 \x81\x75*,\x90\xda\x94\xf6\x81\x76\x82\xcc\x8c\xe3\x82\xcc\x81\x75\x96\xbc\x8e\x8c\x81\x76\x82\xcd\x95\xca\x82\xcc\x83\x41\x83\x4e\x83\x5a\x83\x93\x83\x67\x8b\xe5\x82\xc9
  Rule 11 \x81\x75\x8c\x60\x97\x65\x8e\x8c,\x94\xf1\x8e\xa9\x97\xa7\x81\x76\x82\xcd\x81\x75\x93\xae\x8e\x8c,\x98\x41\x97\x70*\x81\x76or\x81\x75\x8c\x60\x97\x65\x8e\x8c,\x98\x41\x97\x70*\x81\x76or\x81\x75\x8f\x95\x8e\x8c,\x90\xda\x91\xb1\x8f\x95\x8e\x8c,\x82\xc4\x81\x76or\x81\x75\x8f\x95\x8e\x8c,\x90\xda\x91\xb1\x8f\x95\x8e\x8c,\x82\xc5\x81\x76\x82\xc9\x90\xda\x91\xb1\x82\xb7\x82\xe9\x8f\xea\x8d\x87\x82\xc9\x91\x4f\x82\xc9\x82\xad\x82\xc1\x82\xc2\x82\xaf\x82\xe9
  Rule 12 \x81\x75\x93\xae\x8e\x8c,\x94\xf1\x8e\xa9\x97\xa7\x81\x76\x82\xcd\x81\x75\x93\xae\x8e\x8c,\x98\x41\x97\x70*\x81\x76or\x81\x75\x96\xbc\x8e\x8c,\x83\x54\x95\xcf\x90\xda\x91\xb1\x81\x76\x82\xc9\x90\xda\x91\xb1\x82\xb7\x82\xe9\x8f\xea\x8d\x87\x82\xc9\x91\x4f\x82\xc9\x82\xad\x82\xc1\x82\xc2\x82\xaf\x82\xe9
  Rule 13 \x81\x75\x96\xbc\x8e\x8c\x81\x76\x82\xcc\x8c\xe3\x82\xc9\x81\x75\x93\xae\x8e\x8c\x81\x76or\x81\x75\x8c\x60\x97\x65\x8e\x8c\x81\x76or\x81\x75\x96\xbc\x8e\x8c,\x8c\x60\x97\x65\x93\xae\x8e\x8c\x8c\xea\x8a\xb2\x81\x76\x82\xaa\x82\xab\x82\xbd\x82\xe7\x95\xca\x82\xcc\x83\x41\x83\x4e\x83\x5a\x83\x93\x83\x67\x8b\xe5\x82\xc9
  Rule 14 \x81\x75\x8b\x4c\x8d\x86\x81\x76\x82\xcd\x92\x50\x93\xc6\x82\xcc\x83\x41\x83\x4e\x83\x5a\x83\x93\x83\x67\x8b\xe5\x82\xc9
  Rule 15 \x81\x75\x90\xda\x93\xaa\x8e\x8c\x81\x76\x82\xcd\x92\x50\x93\xc6\x82\xcc\x83\x41\x83\x4e\x83\x5a\x83\x93\x83\x67\x8b\xe5\x82\xc9
  Rule 16 \x81\x75*,*,*,\x90\xa9\x81\x76\x82\xcc\x8c\xe3\x82\xcc\x81\x75\x96\xbc\x8e\x8c\x81\x76\x82\xcd\x95\xca\x82\xcc\x83\x41\x83\x4e\x83\x5a\x83\x93\x83\x67\x8b\xe5\x82\xc9
  Rule 17 \x81\x75\x96\xbc\x8e\x8c\x81\x76\x82\xcc\x8c\xe3\x82\xcc\x81\x75*,*,*,\x96\xbc\x81\x76\x82\xcd\x95\xca\x82\xcc\x83\x41\x83\x4e\x83\x5a\x83\x93\x83\x67\x8b\xe5\x82\xc9
  Rule 18 \x81\x75*,\x90\xda\x94\xf6\x81\x76\x82\xcd\x91\x4f\x82\xc9\x82\xad\x82\xc1\x82\xc2\x82\xaf\x82\xe9
*/

#define NJD_SET_ACCENT_PHRASE_MEISHI "\x96\xbc\x8e\x8c"
#define NJD_SET_ACCENT_PHRASE_KEIYOUSHI "\x8c\x60\x97\x65\x8e\x8c"
#define NJD_SET_ACCENT_PHRASE_DOUSHI "\x93\xae\x8e\x8c"
#define NJD_SET_ACCENT_PHRASE_FUKUSHI "\x95\x9b\x8e\x8c"
#define NJD_SET_ACCENT_PHRASE_SETSUZOKUSHI "\x90\xda\x91\xb1\x8e\x8c"
#define NJD_SET_ACCENT_PHRASE_RENTAISHI "\x98\x41\x91\xcc\x8e\x8c"
#define NJD_SET_ACCENT_PHRASE_JODOUSHI "\x8f\x95\x93\xae\x8e\x8c"
#define NJD_SET_ACCENT_PHRASE_JOSHI "\x8f\x95\x8e\x8c"
#define NJD_SET_ACCENT_PHRASE_KIGOU "\x8b\x4c\x8d\x86"
#define NJD_SET_ACCENT_PHRASE_KEIYOUDOUSHI_GOKAN "\x8c\x60\x97\x65\x93\xae\x8e\x8c\x8c\xea\x8a\xb2"
#define NJD_SET_ACCENT_PHRASE_FUKUSHI_KANOU "\x95\x9b\x8e\x8c\x89\xc2\x94\x5c"
#define NJD_SET_ACCENT_PHRASE_SETSUBI "\x90\xda\x94\xf6"
#define NJD_SET_ACCENT_PHRASE_HIJIRITSU "\x94\xf1\x8e\xa9\x97\xa7"
#define NJD_SET_ACCENT_PHRASE_RENYOU "\x98\x41\x97\x70"
#define NJD_SET_ACCENT_PHRASE_SETSUZOKUJOSHI "\x90\xda\x91\xb1\x8f\x95\x8e\x8c"
#define NJD_SET_ACCENT_PHRASE_SAHEN_SETSUZOKU "\x83\x54\x95\xcf\x90\xda\x91\xb1"
#define NJD_SET_ACCENT_PHRASE_TE "\x82\xc4"
#define NJD_SET_ACCENT_PHRASE_DE "\x82\xc5"
#define NJD_SET_ACCENT_PHRASE_SETTOUSHI "\x90\xda\x93\xaa\x8e\x8c"
#define NJD_SET_ACCENT_PHRASE_SEI "\x90\xa9"
#define NJD_SET_ACCENT_PHRASE_MEI "\x96\xbc"

NJD_SET_ACCENT_PHRASE_RULE_H_END;

#endif                          /* !NJD_SET_ACCENT_PHRASE_RULE_H */
