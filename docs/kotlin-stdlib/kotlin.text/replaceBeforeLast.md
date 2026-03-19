

# replaceBeforeLast

Replace part of string before the last occurrence of given delimiter with the replacement string. If the string does not contain the delimiter, returns missingDelimiterValue which defaults to the original string.

```kotlin
fun String.replaceBeforeLast(delimiter: Char, replacement: String, missingDelimiterValue: String = this): String(source)
```

```kotlin
val original = "/home/user/docs/report.txt"

val updated = original.replaceBeforeLast('/', "data")
println(updated)          // prints: "/data/docs/report.txt"

val noDelimiter = "filename"
val unchanged = noDelimiter.replaceBeforeLast('#', "oops")
println(unchanged)       // prints: "filename"
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/replace-before-last.html)

    