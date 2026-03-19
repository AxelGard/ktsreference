

# useContents

Calls the block with temporary copy of this value as receiver.

```kotlin
inline fun <T : CStructVar, R> CValue<T>.useContents(block: T.() -> R): R(source)
```

```kotlin
import kotlinx.cinterop.*
import platform.posix.*

@CStruct("MyStruct")
external class MyStructVar : CStructVar {
    var field1: CInt
    var field2: CDouble
}

fun main() {
    // Create a CValue<MyStructVar> with field values
    val myStruct = cValue<MyStructVar> {
        field1 = 10
        field2 = 2.5
    }

    // Use the struct's contents inside a block
    myStruct.useContents {
        println("field1 = $field1")
        println("field2 = $field2")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/use-contents.html)

    