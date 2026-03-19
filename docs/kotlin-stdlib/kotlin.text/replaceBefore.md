

# replaceBefore

Replace part of string before the first occurrence of given delimiter with the replacement string. If the string does not contain the delimiter, returns missingDelimiterValue which defaults to the original string.

```kotlin
fun String.replaceBefore(delimiter: Char, replacement: String, missingDelimiterValue: String = this): String(source)
```

```kotlin
val original = "apple,banana,cherry"
val modified = original.replaceBefore(',', "fruit:") // result: "fruit:banana,cherry"

val noDelimiter = "apple"
val unchanged = noDelimiter.replaceBefore('|', "prefix:") // result: "apple"
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/replace-before.html)

    