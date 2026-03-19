

# lines

Splits this char sequence to a list of lines delimited by any of the following character sequences: CRLF, LF or CR.

```kotlin
fun CharSequence.lines(): List<String>(source)
```

```kotlin
val text = "Line1\nLine2\r\nLine3\rLine4"
val lines = text.lines()
println(lines)  // [Line1, Line2, Line3, Line4]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/lines.html)

    