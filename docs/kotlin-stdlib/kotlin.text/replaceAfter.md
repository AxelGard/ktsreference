

# replaceAfter

Replace part of string after the first occurrence of given delimiter with the replacement string. If the string does not contain the delimiter, returns missingDelimiterValue which defaults to the original string.

```kotlin
fun String.replaceAfter(delimiter: Char, replacement: String, missingDelimiterValue: String = this): String(source)
```

```kotlin
val original = "hello world"

val replaced1 = original.replaceAfter(' ', "there")          // "hello there"
val replaced2 = original.replaceAfter('x', "nothing")       // "hello world"
val replaced3 = original.replaceAfter('x', "nothing", "no delimiter") // "no delimiter"
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/replace-after.html)

    