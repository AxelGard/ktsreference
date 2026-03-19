

# appendLine

Appends a line feed character (\n) to this Appendable.

```kotlin
@IgnorableReturnValueinline fun Appendable.appendLine(): Appendable(source)
```

```kotlin
fun main() {
    val sb = StringBuilder()
    sb.append("First line")
      .appendLine()
    sb.append("Second line")
      .appendLine()
    println(sb.toString())
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/append-line.html)

    