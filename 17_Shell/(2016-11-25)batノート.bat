
: SJIS(Western Windows1252)�ŕۑ����邱��

: ���܂��Ȃ� 
@echo off
cd /d %~dp0
setlocal enabledelayedexpansion

: for��
:     (�I�v�V�����Ȃ�) �f�B���N�g������ΏۂɂƂ�
:     /d �f�B���N�g������ΏۂɂƂ�
:     /r �f�B���N�g��������т��̃T�u�f�B���N�g������ΏۂɂƂ�
:     /l �l���w�肵�đ��
:     /f �e�L�X�g�t�@�C�����̕��͂ɑ΂���

: dir
:     /a �t�@�C����\������ /ad�Ńf�B���N�g���A/ah�ŉB���t�@�C���A-������Ƃ��̑����ȊO
:     /b �t�@�C�����̂ݕ\��
:     /o �\���� n���O�� s�T�C�Y��(������������) e(�g���q���A�A���t�@�x�b�g) d(�Â�������) g(�f�B���N�g������) -����΋t�� /o-d����Ȋ���


: find
:     /v �w�肵����������܂܂Ȃ�
:     /c �w�蕶������܂ލs��
:     /n �o�͂���s�̑O�ɍs�ԍ�������
:     /i �������啶������ʂ��Ȃ�
find /v /c /n /i "����������" �t�@�C����

: �f�B���N�g�����̃f�B���N�g������COUNT�֊i�[����
: http://capm-network.com/?tag=Windows%E3%83%90%E3%83%83%E3%83%81%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E5%AE%9F%E8%A1%8C%E7%B5%90%E6%9E%9C%E3%81%AE%E5%8F%96%E5%BE%97
for /f "usebackq" %%i in (`dir /ad /b "D:\01_Backup" ^| find /c /v ""`) do (
    set COUNT=%%i
)

: �f�B���N�g�����ň�ԌÂ��f�B���N�g�����擾���� �V�����̂��悩������/o-d��/od�ɂ��Ă�
: delims=�͔z��(?)�̋�؂�����߂Ă�B�f�t�H���g�ł̓X�y�[�X���܂܂�邩��A�V�����t�H���_ (1)�ňُ킪�o��
set OLDEST=
for /f "usebackq delims=" %%i in (`dir D:\01_Backup /ad /o-d /b`) do ( set OLDEST=%%i )
echo !OLDEST!

: �[�����߂����������擾����
set T=%time: =0% (���ꂪ�[������)
echo %T:~0,2%.%T:~3,2%.%T:~6,2%.

: if���̔�r���Z�q
: A equ B    ==
: A neq B    !=
: A gtr B    >
: A geq B    >=
: A lss B    <
: A leq B    <=

: �X���[�v�ɂȂ�܂ł̎��Ԃ��R���g���[������
POWERCFG -x -standby-timeout-ac 0
POWERCFG -x -standby-timeout-dc 0
: 0�Ȃ�X���[�v�Ȃ�

: �܂������Ȏ���ɂ��A�ϐ��̑O��ɂ͂�����������s�v�ȃX�y�[�X����菜�����@
call :Foo !COUNT!
exit
:Foo
set COUNT=%*
: �ŏ�COUNT��"2 "�������Ƃ��Ă�"2"�ɂȂ�
: :Foo��exit��艺�ɏ�������


endlocal
