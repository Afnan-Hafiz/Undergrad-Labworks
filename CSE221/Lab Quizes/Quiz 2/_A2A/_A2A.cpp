#include<bits/extc++.h>
#include<windows.h>
using namespace std;
mt19937 rng;
chrono::system_clock::time_point start, finish;
int test = 0, best = 0, score = 0, batch = 0, total = 0, timeLimit = 0;
string TID, UID, LNG, comment, content, word;
DWORD TLE = 9, errorCode = 0;
char cmd[64];
inline void runSolution() {
    PROCESS_INFORMATION processInfo;
    STARTUPINFOA startupInfo = { sizeof(STARTUPINFOA) };
    SECURITY_ATTRIBUTES securityAttr = {
        sizeof(SECURITY_ATTRIBUTES), NULL, TRUE };
    HANDLE hInput = CreateFileA("in.txt", GENERIC_READ, FILE_SHARE_READ,
        &securityAttr, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
    HANDLE hOutput = CreateFileA("out.txt", GENERIC_WRITE, FILE_SHARE_WRITE,
        &securityAttr, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    if (hInput == INVALID_HANDLE_VALUE || hOutput == INVALID_HANDLE_VALUE)
        return (void)(cout << "Failed to handle stdio\n", errorCode = -1);
    startupInfo.dwFlags |= STARTF_USESTDHANDLES;
    startupInfo.hStdInput = hInput, startupInfo.hStdOutput = hOutput;
    startupInfo.hStdError = GetStdHandle(STD_ERROR_HANDLE);
    HANDLE hJob = CreateJobObject(NULL, NULL);
    if (!hJob)
        return (void)(cout << "Failed to CreateJobObject()\n", errorCode = -1);
    if (!CreateProcessA(NULL, cmd, NULL, NULL, TRUE,
        CREATE_SUSPENDED, NULL, NULL, &startupInfo, &processInfo))
        return (void)(cout << "Failed to CreateProcessA()\n", errorCode = -1);
    if (!AssignProcessToJobObject(hJob, processInfo.hProcess)) {
        TerminateProcess(processInfo.hProcess, errorCode = -1);
        return (void)(cout << "Failed to AssignProcessToJobObject()\n");
    }
    ResumeThread(processInfo.hThread);
    if (WaitForSingleObject(processInfo.hProcess, timeLimit)
        != WAIT_OBJECT_0) TerminateJobObject(hJob, TLE);
    GetExitCodeProcess(processInfo.hProcess, &errorCode); CloseHandle(hInput);
    CloseHandle(hOutput); CloseHandle(processInfo.hThread);
    CloseHandle(processInfo.hProcess); CloseHandle(hJob);
}
inline void endBatch(string verdict) {
    if ((errorCode = verdict != "Accepted") &&
        ifstream(verdict + ".txt").peek() == ifstream::traits_type::eof()) {
        getline(ifstream("in.txt"), content, '\0');
        (ofstream(verdict + ".txt") << content).close();
    }
    cout << fixed << setprecision(9) << "Batch " << batch << " ended in " <<
        (chrono::duration_cast<chrono::nanoseconds>(finish - start).count()
            * 1e-9) << "s and the result is: " + verdict + "\n";
}
inline void updateSubmission() {
    system(("echo " + comment + to_string(score) + " " + UID +
        " %COMPUTERNAME% %USERNAME%>" + TID + "_" + UID + "." + LNG).c_str());
    getline(ifstream("Solution." + LNG), content, '\0');
    (ofstream(TID + "_" + UID + "." + LNG, ios::app) << content).close();
    cout << "Submission updated: " << TID + "_" + UID + "." + LNG << endl;
}
inline void printScoreAndExit() {
    cout << "\nTentative score = " << double(score) / max(total, 1) << "/1\n\n";
    exit(0);
}
int cpp = 2000, java = 3000, py = 6000, nBatch = 10, tn9 = 1000000000;
int weight[] = { 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
int nTest[] = { 0, 2, 2, 20, 20, 20, 20000, 2000, 200, 20, 2 };
int maxN[] = { 0, 5, 10, 100, 1000, 10000, 100, 1000, 10000, 100000, 1000000 };
int maxS[] = { 0, 10, 100, tn9, tn9, tn9, tn9, tn9, tn9, tn9, tn9 };
int maxAi[] = { 0, 10, 100, tn9, tn9, tn9, tn9, tn9, tn9, tn9, tn9 };
int outputHash[] = { 0, 18182, 18182, 57412, 57857, 33827,
    32369, 27996, 52499, 17048, 54558 };
vector<string> OutputC, OutputD;
vector<int> InputN, InputS;
vector<vector<int>> InputA;
inline int getRandInt(int low, int high) {
    return uniform_int_distribution<int>(low, high)(rng);
}
inline void prepareInput() {
    if (batch == 1) {
        InputN = { 4, 4 };
        InputS = { 10, 7 };
        InputA = { {1, 3, 5, 7}, {2, 4, 6, 8} };
    }
    else if (batch == 2) {
        InputN = { 6, 4 };
        InputS = { 18, 10 };
        InputA = { {1, 5, 8, 9, 9, 10}, {1, 5, 6, 8} };
    }
    else {
        InputN.resize(nTest[batch]);
        InputS.resize(nTest[batch]);
        InputA.resize(nTest[batch]);
        for (test = 0; test < nTest[batch]; ++test) {
            int N = InputN[test] = getRandInt(1, maxN[batch]);
            InputS[test] = getRandInt(1, maxS[batch]);
            InputA[test].resize(InputN[test]);
            for (int i = 0; i < N; ++i)
                if (InputA[test][i] = getRandInt(1, maxAi[batch] / N), i)
                    InputA[test][i] += InputA[test][i - 1] - 1;
            if (getRandInt(0, 1) & 1) {
                int i = getRandInt(0, N - 1), j = getRandInt(0, N - 1);
                if (i != j) InputS[test] = InputA[test][i] + InputA[test][j];
            }
        }
    }
    ofstream fout("in.txt");
    for (fout << nTest[batch] << "\n", test = 0; test < nTest[batch]; ++test) {
        fout << InputN[test] << " " << InputS[test] << "\n";
        for (int i = 0; i < InputN[test]; ++i)
            fout << InputA[test][i] << (i + 1 < InputN[test] ? " " : "\n");
    }
    fout.close();
}
int base = 257, mod = 65537;
inline int getHash(string str, int ret = 0) {
    for (auto& c : str) ret = (ret * base + int(c)) % mod;
    return ret;
}
inline int getHash(vector<string> vec, int ret = 0) {
    for (auto& str : vec) ret = (ret * base + getHash(str)) % mod;
    return ret;
}
inline void assertThrow(bool condition) {
    if (!condition) throw exception();
}
inline void validateOutput() {
    try {
        OutputC.clear(), OutputD.clear();
        for (ifstream fin("out.txt"); fin >> word; OutputC.push_back(word))
            if (word == "-1") OutputD.push_back("0");
            else OutputD.push_back("-1");
        assertThrow(getHash(OutputD) == outputHash[batch]);
        // system("pause");
        // cout << getHash(OutputD) << endl;
        for (int k = test = 0; test < nTest[batch]; ++k, ++test)
            if (OutputC[k] != "-1") assertThrow(InputS[test]
                == InputA[test][stoi(OutputC[k]) - 1] +
                InputA[test][stoi(OutputC[k + 1]) - 1]), ++k;
    }
    catch (...) {
        endBatch("WrongAnswer");
    }
}
int main(int argc, char** argv) {
    TID = argv[1], UID = argv[2], LNG = argv[3];
    if (LNG == "cpp") timeLimit = cpp, strcpy(cmd, "b.exe");
    else if (LNG == "java") timeLimit = java, strcpy(cmd, "java Solution");
    if (LNG != "py") comment = "// ";
    else comment = "## ", timeLimit = py, strcpy(cmd, "pypy Solution.py");
    if (!ifstream(TID + "_" + UID + "." + LNG)) updateSubmission();
    getline(ifstream("Solution." + LNG), content, '\0');
    for (char& c : content) c = tolower(c);
    for (ifstream fin(TID + "_Forbidden.txt"); fin >> word;)
        if (content.find(word) != string::npos)
            cout << "ForbiddenKeyword: " << word << "\n", printScoreAndExit();
    if ((LNG == "cpp" && system("c++ Solution.cpp -o b.exe")) ||
        (LNG == "java" && system("javac Solution.java")) ||
        (LNG == "py" && system("pypy -m py_compile Solution.py")))
        cout << "CompilationError\n", printScoreAndExit();
    for (string& s : vector<string>({ "RunTimeError",
        "TimeLimitExceeded", "WrongAnswer" })) ofstream(s + ".txt").close();
    ifstream(TID + "_" + UID + "." + LNG).ignore(3) >> best;
    for (batch = 1; batch <= nBatch; errorCode = 0, total += weight[batch++]) {
        rng.seed(batch), cout << "Running on Batch " << batch << endl;
        prepareInput(), start = chrono::high_resolution_clock::now();
        runSolution(), finish = chrono::high_resolution_clock::now();
        if (errorCode == TLE) endBatch("TimeLimitExceeded");
        else if (errorCode) endBatch("RunTimeError");
        else if (validateOutput(), !errorCode && (endBatch("Accepted"),
            best <= (score += weight[batch]))) updateSubmission();
    }
    cout.unsetf(ios::fixed), printScoreAndExit();
}