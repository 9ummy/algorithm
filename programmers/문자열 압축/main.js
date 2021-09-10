function solution(s) {
  const answer = [];

  if (s.length === 1) return 1;

  for (let targetLen = 1; targetLen <= Math.floor(s.length / 2); targetLen++) {
    // 타겟 문자열의 길이에 맞게 타겟 문자열 새로 설정
    let target = s.slice(0, targetLen);
    // 타겟 문자열을 새로 설정할 때 압축 결과물을 담을 문자열과 카운트도 리셋해줌
    let compressed = '';
    let count = 1;

    // 앞에서부터 정해진 길이만큼 잘라야 하므로 targetLen만큼 늘어나게 함 (놓쳤던 부분)
    for (let i = targetLen; i < s.length; i += targetLen) {
      // target 문자열의 다음 인덱스부터 타겟 문자열의 길이만큼의 문자열을 비교할 문자열로 설정
      const check = s.slice(i, i + targetLen);

      // 비교할 문자열과 타겟 문자열이 같을 경우
      if (check === target) {
        // 압축 횟수를 세는 카운트 증가
        count++;
      } else {
        // 다를 경우 압축한 횟수를 확인해서 압축 결과 문자열에 담아줌
        // 1회 등장할 경우 압축 X, 압축 횟수 표시 X 이므로 카운트에 빈 문자열을 담아 숫자가 들어가지 않도록
        if (count === 1) count = '';
        compressed += count + target;
        // 타겟 문자열을 현재 비교 중인 문자열로 변경해줌
        target = check;
        count = 1;
      }
    }
    // 압축 문자열에 담기지 않은 나머지 문자열을 담아줌
    if (count === 1) count = '';
    compressed += count + target;
    answer.push(compressed.length);
  }

  return Math.min(...answer);
}
