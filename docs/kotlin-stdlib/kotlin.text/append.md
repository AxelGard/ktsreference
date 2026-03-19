

# append

Appends all arguments to the given Appendable.

```kotlin
@IgnorableReturnValuefun <T : Appendable> T.append(vararg value: CharSequence?): T(source)
```

```kotlin
fun main() {
    val sb = StringBuilder()
    sb.append("Hello", " ", "World", "!")
    println(sb.toString())
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/append.html)

    