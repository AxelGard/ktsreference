

# insert

Inserts the string representation of the specified byte value into this string builder at the specified index and returns this instance.

```kotlin
@IgnorableReturnValueexpect fun StringBuilder.insert(index: Int, value: Byte): StringBuilder(source)
```

```kotlin
fun main() {
    val sb = StringBuilder("Hello")
    sb.insert(5, 65.toByte())   // inserts the string representation of the byte value
    println(sb)                  // prints: Hello65
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/insert.html)

    