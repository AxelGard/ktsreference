

# appendln

Warning since 1.4

```kotlin
fun Appendable.appendln(): Appendable(source)
```

```kotlin
fun main() {
    val sb = StringBuilder()
    sb.append("First line")
    sb.appendln()
    sb.append("Second line")
    sb.appendln()
    println(sb.toString())
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/appendln.html)

    